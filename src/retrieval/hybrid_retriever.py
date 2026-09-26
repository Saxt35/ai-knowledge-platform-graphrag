# Hybrid Retriever - Vector + Graph

def hybrid_retrieve(query: str):
    # 1. Vector search top-k
    vector_results = vector_store.similarity_search(query, k=20)
    # 2. Graph expansion via SPARQL
    graph_results = jena_store.sparql_expand(vector_results)
    # 3. Re-rank
    reranked = reranker.rerank(query, vector_results + graph_results)
    # 4. Validate
    validated = sparql_validator.validate(reranked)
    return validated