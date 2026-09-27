# ADR 003: Hybrid Retrieval - Vector + Graph + Re-ranker

## Decisión
Retriever híbrido en lugar de solo vectorial.

## Flujo
1. Query -> embedding
2. Vector Store (FAISS/Azure Search) top-k=20
3. Graph Store (Jena) expansión via SPARQL de entidades relacionadas
4. Re-ranker cross-encoder
5. SPARQL Validator: verifica que respuesta esté soportada por grafo

## Beneficio
Reduce alucinación en preguntas multi-salto tipo: "Qué clientes conectados a este riesgo vía 3 empresas"