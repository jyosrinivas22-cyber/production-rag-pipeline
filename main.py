import yaml
from dotenv import load_dotenv

from src.caching.exact_cache import ExactCache
from src.caching.semantic_cache import SemanticCache
from src.caching.retrieval_cache import RetrievalCache

from src.retrieval.retriever import retrieve_documents
from src.generation.generator import generate_answer

load_dotenv()

config = yaml.safe_load(open("config.yaml"))

exact_cache = ExactCache()
semantic_cache = SemanticCache(config["caching"]["semantic_threshold"])
retrieval_cache = RetrievalCache()


def process_query(query):

    # Tier 1
    result = exact_cache.get(query)
    if result:
        print("Exact Cache Hit")
        return result

    # Tier 2
    result = semantic_cache.search(query)
    if result:
        print("Semantic Cache Hit")
        return result

    # Tier 3
    docs = retrieval_cache.get(query)
    if docs:
        print("Retrieval Cache Hit")
        answer = generate_answer(query, docs)
        return answer

    # Full pipeline
    print("Running Full Pipeline")

    docs = retrieve_documents(query)

    answer = generate_answer(query, docs)

    exact_cache.store(query, answer)
    semantic_cache.store(query, answer)
    retrieval_cache.store(query, docs)

    return answer


if __name__ == "__main__":

    while True:
        q = input("Ask: ")
        print(process_query(q))
