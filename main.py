from identify_ticker import identify_ticker
from ticker_price import get_current_price
from ticker_price_change import get_price_change
from ticker_news import get_stock_news
from ticker_analysis import analyze_stock_movement

def run_query(query):
    ticker = identify_ticker(query)
    if not ticker:
        return "❌ Couldn't find a stock ticker in your query."

    print(f"✅ Identified ticker: {ticker}")

    if "price change" in query or "changed" in query:
        return get_price_change(ticker, 7)
    
    elif "price" in query:
        return get_current_price(ticker)
    
    elif "news" in query or "happening" in query:
        company_name = input("Enter company name for news: ")
        return get_stock_news(company_name)
    
    elif "why" in query or "analysis" in query:
        company_name = input("Enter company name for analysis: ")
        return analyze_stock_movement(ticker, company_name, 3)

    else:
        return "🤖 Sorry, I couldn't understand your query type."

# Main loop
if __name__ == "__main__":
    print("💬 Ask me about a stock! (e.g., 'Why did Tesla drop today?')")
    print("📌 Type 'exit' to quit.\n")

    while True:
        q = input("Your question: ")
        if q.lower() == "exit":
            print("👋 Goodbye!")
            break

        result = run_query(q)

        print("\n🧾 Response:\n")
        if isinstance(result, dict):  # for price change
            print(f"- {result['past_date']}: ${result['past_price']}")
            print(f"- {result['latest_date']}: ${result['latest_price']}")
            print(f"- Change: ${result['change']} ({result['percent']:.2f}%)")
        elif isinstance(result, list):  # for news
            for title, url in result:
                print(f"- {title}\n  🔗 {url}")
        else:
            print(result)

        print("\n🔁 Ask another question or type 'exit' to stop.\n")
