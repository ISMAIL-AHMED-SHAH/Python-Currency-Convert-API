
import streamlit as st
import requests

# --- Page Config ---
st.set_page_config(page_title="💱 Currency Converter", layout="centered")

# --- Title ---
st.title("💱 Real-Time Currency Converter")
st.markdown("Easily convert between currencies using live exchange rates 🌍")

# --- Input Fields ---
amount = st.number_input("Enter Amount", min_value=0.0, format="%.2f")

# Fetch currency list from API
@st.cache_data
def get_currency_list():
    url = "https://api.exchangerate-api.com/v4/latest/PKR"
    try:
        response = requests.get(url)
        data = response.json()
        return sorted(list(data.keys()))
    except Exception as e:
        st.error(f"⚠️ Error fetching currency list: {e}")
        return []



currencies = get_currency_list()

if not currencies:
    st.stop()  # Stop execution if currencies not loaded

# Handle default selection safely
default_from = currencies.index("USD") if "USD" in currencies else 0
default_to = currencies.index("PKR") if "PKR" in currencies else 1

from_currency = st.selectbox("From Currency", currencies, index=default_from)
to_currency = st.selectbox("To Currency", currencies, index=default_to)




# --- Conversion Logic ---
if st.button("🔁 Convert"):
    with st.spinner("Fetching exchange rate..."):
        try:
            url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
            response = requests.get(url)
            data = response.json()

            # Get the converted amount
            result = data["rates"][to_currency]

            # Calculate exchange rate
            rate = result / amount if amount != 0 else 0

            st.success(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
            st.caption(f"Exchange Rate: 1 {from_currency} = {rate:.4f} {to_currency}")
        except Exception as e:
            st.error(f"❌ Failed to fetch conversion rate: {e}")


