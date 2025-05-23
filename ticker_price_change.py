# ticker_price_change.py
import requests
from datetime import datetime, timedelta

# ⛳ Use your Alpha Vantage API key
API_KEY = "JIZCV40Y8RQOANE1"

def get_price_change(ticker, days_back=1):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": ticker,
        "apikey": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    try:
        prices = data["Time Series (Daily)"]
        dates = sorted(prices.keys(), reverse=True)

        latest_date = dates[0]
        past_date = dates[days_back]

        latest_price = float(prices[latest_date]["4. close"])
        past_price = float(prices[past_date]["4. close"])
        change = latest_price - past_price
        percent = (change / past_price) * 100

        return {
            "ticker": ticker,
            "latest_date": latest_date,
            "latest_price": latest_price,
            "past_date": past_date,
            "past_price": past_price,
            "change": change,
            "percent": percent
        }
    except Exception as e:
        print("Error:", e)
        return None

# Test
if __name__ == "__main__":
    ticker = input("Enter stock ticker (e.g., TSLA): ").upper()
    days = input("Compare with how many days ago? (e.g., 1 or 7): ")

    try:
        days_back = int(days)
    except:
        days_back = 1

    result = get_price_change(ticker, days_back)

    if result:
        print(f"\n📈 Price change for {ticker} over {days_back} day(s):")
        print(f"- {result['past_date']}: ${result['past_price']:.2f}")
        print(f"- {result['latest_date']}: ${result['latest_price']:.2f}")
        print(f"- Change: ${result['change']:.2f} ({result['percent']:.2f}%)")
    else:
        print("❌ Could not fetch price change.")
