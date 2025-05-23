# ticker_analysis.py

from ticker_price_change import get_price_change
from ticker_news import get_stock_news

def analyze_stock_movement(ticker, company_name, days_back=1):
    # 1. Get price change info
    price_info = get_price_change(ticker, days_back)

    if not price_info:
        return "❌ Couldn't analyze price change."

    # 2. Get recent news
    news = get_stock_news(company_name)
    if not news:
        return "❌ Couldn't fetch news for analysis."

    # 3. Build the summary
    summary = f"""
🧠 Stock Analysis for {ticker} ({company_name}) - Last {days_back} day(s)

📊 Price Movement:
- {price_info['past_date']}: ${price_info['past_price']:.2f}
- {price_info['latest_date']}: ${price_info['latest_price']:.2f}
- Change: ${price_info['change']:.2f} ({price_info['percent']:.2f}%)

📰 Top Headlines:
"""
    for title, url in news:
        summary += f"- {title}\n  🔗 {url}\n"

    summary += "\n📌 Based on the price and news, you may investigate further."

    return summary

# Test
if __name__ == "__main__":
    ticker = input("Enter stock ticker (e.g., TSLA): ").upper()
    company = input("Enter full company name (e.g., Tesla): ")
    days = input("Compare with how many days ago? (e.g., 1 or 7): ")

    try:
        days_back = int(days)
    except:
        days_back = 1

    result = analyze_stock_movement(ticker, company, days_back)
    print(result)
