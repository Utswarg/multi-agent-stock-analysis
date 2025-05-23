# identify_ticker.py
import re

# Simple map of company names to ticker symbols
company_to_ticker = {
    "tesla": "TSLA",
    "nvidia": "NVDA",
    "apple": "AAPL",
    "microsoft": "MSFT",
    "amazon": "AMZN",
    "google": "GOOGL",
    "alphabet": "GOOGL",
    "meta": "META",
    "facebook": "META",
    "palantir": "PLTR",
}

def identify_ticker(query):
    query_lower = query.lower()
    
    # 1. Check company name in query
    for company in company_to_ticker:
        if company in query_lower:
            return company_to_ticker[company]

    # 2. Check for ticker symbol directly (e.g., TSLA, NVDA)
    ticker_match = re.findall(r"\b[A-Z]{2,5}\b", query)
    if ticker_match:
        return ticker_match[0]  # Return first match

    return None

# Test
if __name__ == "__main__":
    q = input("Ask: ")
    print("Ticker:", identify_ticker(q))
