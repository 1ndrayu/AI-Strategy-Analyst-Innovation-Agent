from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def search_reddit(query, max_posts=5):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        search_url = f"https://www.reddit.com/search/?q={query.replace(' ', '%20')}"
        page.goto(search_url)
        page.wait_for_timeout(3000)  # Wait 3 seconds for JS to load

        content = page.content()
        soup = BeautifulSoup(content, "html.parser")

        # Extract post titles and excerpts
        posts = []
        for div in soup.find_all("div", {"data-testid": "post-container"})[:max_posts]:
            title = div.find("h3")
            if title:
                posts.append(title.text.strip())

        browser.close()
        return posts
