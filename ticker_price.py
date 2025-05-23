# ticker_price.py
import requests

# ⛳ Paste your API key here!
API_KEY = "JIZCV40Y8RQOANE1"

def get_current_price(ticker):
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": ticker,
        "apikey": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    try:
        price = data["Global Quote"]["05. price"]
        return float(price)
    except:
        return None

# Testing it
if __name__ == "__main__":
    ticker = input("Enter stock ticker (e.g., TSLA): ").upper()
    price = get_stock_price(ticker)
    if price:
        print(f"✅ Current price of {ticker} is ${price:.2f}")
    else:
        print("❌ Couldn't fetch price. Try again or check the ticker/API key.")
