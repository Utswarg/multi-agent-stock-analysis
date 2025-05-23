# ticker_news.py
import requests

# ⛳ Paste your News API key here
API_KEY = "9e5804f47a37462ba6686fdc6d1ea30d"

def get_stock_news(company_name):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": company_name,
        "sortBy": "publishedAt",
        "apiKey": API_KEY,
        "pageSize": 5  # Top 5 recent articles
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["status"] == "ok":
        articles = data["articles"]
        return [(article["title"], article["url"]) for article in articles]
    else:
        return None

# Test it
if __name__ == "__main__":
    company = input("Enter company name (e.g., Tesla): ")
    news_list = get_stock_news(company)

    if news_list:
        print(f"\n📰 Recent news about {company}:\n")
        for title, url in news_list:
            print(f"- {title}\n  🔗 {url}\n")
    else:
        print("❌ Could not fetch news.")
