import streamlit as st
import requests

# --- Page Config ---
st.set_page_config(page_title="💱 Currency Converter", layout="centered")

st.image("currency.jpg", use_container_width=True)

# --- Title ---
st.title("💱 Real-Time Currency Converter")
st.markdown("Easily convert between currencies using live exchange rates 🌍")

# --- Input Fields ---
amount = st.number_input("Enter Amount", min_value=0.0, format="%.2f")

# --- Fetch currency list ---
@st.cache_data
def get_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/PKR"
    response = requests.get(url)
    data = response.json()
    return data["rates"]

rates = get_exchange_rates()
currencies = sorted(rates.keys())

# --- Select Currencies ---
from_currency = st.selectbox("From Currency", currencies, index=currencies.index("USD"))
to_currency = st.selectbox("To Currency", currencies, index=currencies.index("PKR"))

# --- Conversion + Reset Buttons in Columns ---
col1, col2 = st.columns([1, 2])

with col1:
    if st.button("🔁 Convert"):
        with st.spinner("Converting..."):
            try:
                if from_currency == "PKR":
                    converted_amount = amount * rates[to_currency]
                    rate_info = rates[to_currency]
                else:
                    amount_in_pkr = amount / rates[from_currency]
                    converted_amount = amount_in_pkr * rates[to_currency]
                    rate_info = converted_amount / amount if amount != 0 else 0

                st.success(f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
                st.caption(f"Exchange Rate: 1 {from_currency} = {rate_info:.4f} {to_currency}")

            except Exception as e:
                st.error(f"❌ Conversion failed: {e}")

with col2:
    if st.button("🔄 Reset"):
        st.session_state.clear()
        st.rerun()


# --- SIDEBAR ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/5940/5940705.png", width=100)

st.sidebar.header("💡 Tips")
st.sidebar.info("💱 Use this app to quickly check currency values using live rates. Choose wisely while travelling!")


st.sidebar.markdown("---")


st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135716.png")
st.sidebar.markdown("<p style='text-align: center; color: grey;'>Built with ❤️ by Ismail Ahmed Shah</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

# --- Contact Section ---
st.sidebar.markdown("### 📬 Contact")
st.sidebar.write("📧 [Email Me Us](mailto:ismailahmedshahpk@gmail.com)")
st.sidebar.write("🔗 [Connect On LinkedIn](https://www.linkedin.com/in/ismail-ahmed-shah-2455b01ba/)")
st.sidebar.write("💬 [Chat On WhatsApp](https://wa.me/923322241405)")

st.sidebar.markdown("---")