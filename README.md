# Search Ranking Math

When you search for something, a search engine has to decide which results to show first. In this project I explore the math behind this decision, step by step: from simple word overlap (Jaccard similarity) to TF-IDF, cosine similarity and BM25. I work with web scraping and Elasticsearch every day, and I wanted to understand how search ranking actually works under the hood.

## Motivation
I work with web scraping and Elasticsearch, where search scores are used to rank documents. I use these scores in my daily work, but I wanted to understand how they are calculated and what happens behind them. I chose this topic because I wanted to connect the math from the course with something I work with in real life.

## Methods
I use 40 English Wikipedia articles about technology, in 4 groups (programming languages, databases, web & scraping, DevOps & tools). I turn each text into lowercase words and remove the stopwords. I only look at which words a text contains, not at their order (this is called bag of words).

I explain three scoring methods with formulas, simple proofs and examples calculated by hand, and then I implement them in plain Python:

1. **Jaccard similarity**: the share of common words between the query and the document (sets).
2. **TF-IDF + cosine similarity**: every word gets a weight (frequent in the document, rare in the collection), and the score is the cosine of the angle between the two vectors. I check my TF-IDF vectors against scikit-learn.
3. **BM25**: the default scoring method of Elasticsearch, with term frequency saturation and document length normalization.

I compare the methods on 12 fixed queries (3 per group) with **Precision@5** and **MRR**. A document counts as relevant if it is in the same group as the query.

## Project structure
```
search_ranking.ipynb   # the main notebook: theory, code, experiments
collect_data.py        # downloads the articles once (not needed to run the notebook)
data/articles.json     # the saved articles, so the results are always the same
requirements.txt       # pinned library versions
```

## How to run
Requires Python 3.12 and Jupyter.

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook search_ranking.ipynb
```

## Results
| Method | mean Precision@5 | MRR |
|---|---|---|
| Jaccard | 0.517 | 0.685 |
| TF-IDF + cosine | 0.750 | 1.000 |
| BM25 | 0.783 | 0.958 |

- Weighting the words (TF-IDF or BM25) works much better than only checking if a word is present (Jaccard).
- The difference between TF-IDF + cosine and BM25 is too small to choose a winner with only 12 queries.
- Our TF-IDF vectors are exactly the same as the ones from scikit-learn, when the same formula is used.

The limitations of the experiment are described in section 8 of the notebook.

## References
1. Wikipedia, The Free Encyclopedia: 40 articles used as the corpus (titles and URLs in `data/articles.json`). Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Retrieved 2026-10-23.
2. [MediaWiki Action API](https://www.mediawiki.org/wiki/API:Main_page): used to download the articles.
3. Paul Jaccard, "Étude comparative de la distribution florale dans une portion des Alpes et du Jura", 1901. See also [Wikipedia: Jaccard index](https://en.wikipedia.org/wiki/Jaccard_index).
4. Karen Spärck Jones, "A statistical interpretation of term specificity and its application in retrieval", Journal of Documentation, 1972. See also [Wikipedia: tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf).
5. Christopher D. Manning, Prabhakar Raghavan, Hinrich Schütze, "Introduction to Information Retrieval", Cambridge University Press, 2008, chapters 1, 6, 8 and 19. [Online version](https://nlp.stanford.edu/IR-book/).
6. [Wikipedia: Cauchy-Schwarz inequality](https://en.wikipedia.org/wiki/Cauchy%E2%80%93Schwarz_inequality).
7. Fabian Pedregosa et al., "Scikit-learn: Machine Learning in Python", Journal of Machine Learning Research 12, 2011. See also [scikit-learn User Guide: Tf-idf term weighting](https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting).
8. Stephen Robertson, Hugo Zaragoza, "The Probabilistic Relevance Framework: BM25 and Beyond", Foundations and Trends in Information Retrieval 3(4), 2009. See also [Wikipedia: Okapi BM25](https://en.wikipedia.org/wiki/Okapi_BM25).
9. [Elasticsearch Reference: Similarity module](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/index-modules-similarity.html).
10. [Apache Lucene 10.3.1 API: BM25Similarity](https://lucene.apache.org/core/10_3_1/core/org/apache/lucene/search/similarities/BM25Similarity.html).
11. [Wikipedia: Mean reciprocal rank](https://en.wikipedia.org/wiki/Mean_reciprocal_rank).
12. Sergey Brin, Lawrence Page, "The anatomy of a large-scale hypertextual Web search engine", Computer Networks and ISDN Systems 30, 1998. See also [Wikipedia: PageRank](https://en.wikipedia.org/wiki/PageRank).

## Tools used
- Python 3.12, NumPy, Matplotlib, scikit-learn, Jupyter Notebook
- I used LLMs (Claude, ChatGPT and Gemini) to help me understand the concepts, explain the main ideas, and write and review the text and code.
