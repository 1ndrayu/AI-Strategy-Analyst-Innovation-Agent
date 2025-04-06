from agent.tools import search_reddit
from agent.analyzer import analyze_content

def run_agent_loop():
    print("🧠 Market Intelligence Agent (GPT4All + Local Scraping)")
    query = input("Enter a product/industry to analyze: ")

    print(f"[1/3] Scraping Reddit for '{query}' discussions...")
    reddit_posts = search_reddit(query)

    if not reddit_posts:
        print("⚠️ No posts found. Try a broader topic.")
        return

    print(f"[2/3] Analyzing {len(reddit_posts)} posts with GPT4All...")
    report = analyze_content(reddit_posts)

    print("\n📊 Final Report:\n")
    print(report)
