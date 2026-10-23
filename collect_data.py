"""Downloads the Wikipedia articles and saves them to data/articles.json."""

import json
import time
import urllib.parse
import urllib.request
from datetime import date

API_URL = "https://en.wikipedia.org/w/api.php"
USER_AGENT = "search-ranking-math/1.0 (https://github.com/N1ko-Gr/search-ranking-math)"
OUTPUT_FILE = "data/articles.json"
PAUSE_SECONDS = 1

ARTICLES = {
    "Programming languages": [
        "Python (programming language)", "Java (programming language)", "JavaScript",
        "C Sharp (programming language)", "C (programming language)", "Go (programming language)",
        "Rust (programming language)", "PHP", "Ruby (programming language)", "SQL",
    ],
    "Databases": [
        "Oracle Database", "PostgreSQL", "MySQL", "SQLite", "Redis",
        "Apache Cassandra", "MongoDB", "Elasticsearch", "NoSQL", "Relational database",
    ],
    "Web & scraping": [
        "Web scraping", "Web crawler", "Selenium (software)", "HTML", "CSS",
        "HTTP", "Proxy server", "Search engine", "Kibana", "REST",
    ],
    "DevOps & tools": [
        "Git", "GitLab", "Docker (software)", "Kubernetes", "Linux",
        "Nginx", "Continuous integration", "Virtual machine", "Bash (Unix shell)", "Jenkins (software)",
    ],
}


def fetch_article(title):
    """Gets the title and text of one article. Returns empty text if the article is not found."""
    params = {
        "action": "query",
        "prop": "extracts",
        "explaintext": 1,
        "redirects": 1,
        "format": "json",
        "titles": title,
    }
    url = API_URL + "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.load(response)

    page = next(iter(data["query"]["pages"].values()))
    if "missing" in page:
        return title, ""
    return page["title"], page.get("extract", "")


def main():
    articles = []
    for group, titles in ARTICLES.items():
        for title in titles:
            final_title, text = fetch_article(title)
            if not text:
                print(f"WARNING: no text for '{title}'")
            else:
                articles.append({
                    "id": len(articles),
                    "group": group,
                    "title": final_title,
                    "url": "https://en.wikipedia.org/wiki/" + final_title.replace(" ", "_"),
                    "text": text,
                })
                print(f"OK: {final_title} ({len(text.split())} words)")
            time.sleep(PAUSE_SECONDS)

    corpus = {
        "source": "English Wikipedia (https://en.wikipedia.org), MediaWiki API",
        "license": "CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)",
        "retrieved": date.today().isoformat(),
        "articles": articles,
    }
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(corpus, f, ensure_ascii=False, indent=1)
    print(f"Saved {len(articles)} articles to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
