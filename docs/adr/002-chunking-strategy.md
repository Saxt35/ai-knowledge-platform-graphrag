# ADR 002: Estrategia de Chunking Semántico

Fecha: 2026-09-25

## Problema
Chunking fijo 1000 tokens perdía contexto y generaba alucinación.

## Decisión
Chunking semántico 400-600 tokens con overlap 15%, jerárquico (doc -> sección -> chunk), con metadata de origen guardada en RDF.

## Implementación
- PySpark job en Zeppelin/Livy
- Relación RDF: Documento -> Sección -> Chunk
- Embeddings OpenAI text-embedding-3-large

## Resultado (HASSERV)
Faithfulness subió de 0.62 a 0.91 en dataset de 100 preguntas doradas.