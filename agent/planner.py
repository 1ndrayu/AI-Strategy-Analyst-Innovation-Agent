from agent.tools import scrape_discussions
from agent.analyzer import analyze_content

def run_agent_loop():
    print("🔍 AI Strategy Analyst is ready.")
    query = input("Enter an industry, market, or product to analyze: ")

    print(f"[*] Scraping content related to '{query}'...")
    text_chunks = scrape_discussions(query)

    print(f"[*] Analyzing content with GPT4All...")
    report = analyze_content(text_chunks)

    print("\n📊 Market Gap Report:\n")
    print(report)
