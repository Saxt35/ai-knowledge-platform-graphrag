# ADR-005: ClickHouse vs Druid
Date: 2025-08-20 | Status: Accepted
Diagrama: tecnologias-soporte-bigdata-platform.png -> OLAP ClickHouse + Metabase

Decisión: ClickHouse.

Justificación:
- Spark 3.x Parquet directo a ClickHouse via JDBC+S3, Druid requiere ingestion spec + MiddleManager
- HDFS+YARN 4 nodes+Airflow ya existentes
- Metabase driver nativo ClickHouse (bloque Metabase diagrama)
- <200ms para JavaScript Node.js Tree.js 3D model

Consecuencias: +120ms p95, +10M rows/min.