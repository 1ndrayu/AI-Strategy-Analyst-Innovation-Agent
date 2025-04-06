from agent.tools import search_web, scrape_reddit
from agent.analyzer import analyze_content

def run_agent_loop():
    print("[*] Planning task...")

    query = input("Enter market or product area: ")
    print(f"[*] Searching web for '{query}'")

    web_data = search_web(query)
    reddit_data = scrape_reddit(query)

    combined = web_data + reddit_data

    print("[*] Analyzing data for market gaps...")
    report = analyze_content(combined)

    print("\n=== Market Gap Report ===\n")
    print(report)
