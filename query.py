from whoosh import index
from whoosh.qparser import QueryParser
from whoosh.scoring import BM25F

def search_index(query_text):
    ix = index.open_dir("indexdir")  # Open index directory
    bm25f = BM25F(B=0.1, K1=2)
    with ix.searcher(weighting=bm25f) as searcher:
        query_parser = QueryParser("content", schema=ix.schema)
        query = query_parser.parse(query_text)
        results = searcher.search(query, limit=25)  # limit=None, filter=True

        # Print query results
        for hit in results:
            print(f"Path: {hit['file']}")
            # print(hit['content'])
            print(f"Score: {hit.score}")
            print("---------------")

if __name__ == "__main__":
    print("Query: ")
    query_text = input()

    search_index(query_text)

    