import streamlit as st
from binance.client import Client

# 바이낸스 연결 및 레퍼럴 설정
client = Client()
my_referral = "https://accounts.binance.info/en/REGISTER?ref=UAUBG73C"

st.set_page_config(page_title="Smart Trader Helper", page_icon="📈")

# 언어 선택
lang = st.selectbox("Select Language", ["English", "한국어", "Tiếng Việt", "हिन्दी"])

# 언어별 문구 설정
msg = {
    "English": {"entry": "Entry Price", "lev": "Leverage", "margin": "Margin", "btn": "Activate Fee Discount", "info": "Trading with optimized fees increases your net profit."},
    "한국어": {"entry": "진입 가격", "lev": "레버리지", "margin": "투자 원금", "btn": "수수료 할인 혜택 활성화", "info": "최적화된 수수료는 실질 수익률을 높여줍니다."},
    "Tiếng Việt": {"entry": "Giá vào", "lev": "Đòn bẩy", "margin": "Số tiền", "btn": "Kích hoạt giảm giá phí", "info": "Giao dịch với phí tối ưu giúp tăng lợi nhuận thuần."},
    "हिन्दी": {"entry": "प्रवेश मूल्य", "lev": "ले버리지", "margin": "निवेश राशि", "btn": "शुल्क छूट सक्रिय करें", "info": "अनुकूलित शुल्क के साथ व्यापार करने से लाभ बढ़ता है।"}
}[lang]

st.title("💰 Profit & ROE Calculator")

# 입력창
col1, col2 = st.columns(2)
with col1:
    entry = st.number_input(msg['entry'], value=60000.0)
with col2:
    lev = st.number_input(msg['lev'], value=10, step=1)
margin = st.number_input(msg['margin'], value=100.0)

# 실시간 시세 및 계산
ticker = client.get_symbol_ticker(symbol="BTCUSDT")
curr = float(ticker['price'])
roe = ((curr - entry) / entry) * lev * 100
profit = margin * (roe / 100)

# 결과 노출
st.divider()
st.subheader(f"Live BTC: ${curr:,.2f}")
st.metric("ROE (%)", f"{roe:.2f}%", delta=f"{roe:.2f}%")
st.write(f"### Estimated Profit: **${profit:,.2f}**")

# 세련된 레퍼럴 유도
st.info(f"💡 {msg['info']}")
st.link_button(f"🚀 {msg['btn']} (Binance Partner)", my_referral, use_container_width=True)
