# Search Ranking Math

When you search for something, a search engine has to decide which results to show first. In this project I explore the math behind this decision, step by step: from simple word overlap (Jaccard similarity) to TF-IDF and cosine similarity. I work with web scraping and Elasticsearch every day, and I wanted to understand how search ranking actually works under the hood.

## Motivation

## Methods

## How to run
Requires Python 3.12 and Jupyter.

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook search_ranking.ipynb
```

## Results

## References
1. Wikipedia, The Free Encyclopedia: 40 articles used as the corpus (titles and URLs in `data/articles.json`). Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Retrieved 2026-10-23.
2. [MediaWiki Action API](https://www.mediawiki.org/wiki/API:Main_page): used to download the articles.
3. Paul Jaccard, "Étude comparative de la distribution florale dans une portion des Alpes et du Jura", 1901. See also [Wikipedia: Jaccard index](https://en.wikipedia.org/wiki/Jaccard_index).
4. Karen Spärck Jones, "A statistical interpretation of term specificity and its application in retrieval", Journal of Documentation, 1972. See also [Wikipedia: tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf).
5. Christopher D. Manning, Prabhakar Raghavan, Hinrich Schütze, "Introduction to Information Retrieval", Cambridge University Press, 2008, chapter 6. [Online version](https://nlp.stanford.edu/IR-book/).
6. [Wikipedia: Cauchy-Schwarz inequality](https://en.wikipedia.org/wiki/Cauchy%E2%80%93Schwarz_inequality).

## Tools used
- Python 3.12, NumPy, Matplotlib, scikit-learn, Jupyter Notebook
- I used LLMs (Claude, ChatGPT and Gemini) to help me understand the concepts, explain the main ideas, and write and review the text and code.
