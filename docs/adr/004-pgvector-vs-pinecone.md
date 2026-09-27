# ADR-004: pgvector vs Pinecone
Date: 2025-08-15 | Status: Accepted | Autor: Noe Briones
Diagrama: tecnologias-soporte-bigdata-platform.png -> PostgreSQL / pgvector

Decisión: pgvector sobre PostgreSQL existente.

Justificación:
- PostgreSQL ya en Infra HADOOP/HUE (diagrama Infrastructure & Tools)
- Pinecone SaaS no permitido COMIMSA/HASSERV (gobernanza)
- Spark-SQL -> JDBC Postgres directo (bloque Ingesta Spark-SQL)
- Mismo Postgres para MDM + vectores

Consecuencias: +85ms p95, costo 0, faithfulness 0.91 mantenido.