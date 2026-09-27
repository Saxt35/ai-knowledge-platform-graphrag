# ai-knowledge-platform-graphrag

> **Diseño conceptual y anonimizado de plataforma empresarial de conocimiento con GraphRAG**
> Faithfulness 0.91 | Hallucinations ↓ | 5 capas | Apache Jena + pgvector + ClickHouse

[[Architecture: 5-Layer](https://img.shields.io/badge/Architecture-5_Layer-blue?style=for-the-badge)](https://github.com/Saxt35/ai-knowledge-platform-graphrag#3-arquitectura-conceptual---tecnologías-soporte)
[[GraphRAG: Faithfulness 0.91](https://img.shields.io/badge/GraphRAG-Faithfulness%200.91-green?style=for-the-badge)](https://github.com/Saxt35/ai-knowledge-platform-graphrag#6-métricas-poc)
[[Stack: Jena+pgvector+ClickHouse](https://img.shields.io/badge/Stack-Jena%2Bpgvector%2BClickHouse-orange?style=for-the-badge)](https://github.com/Saxt35/ai-knowledge-platform-graphrag#5-stack-técnico-mapeado-al-diagrama)
[[Status: Conceptual Anonymized](https://img.shields.io/badge/Status-Conceptual%20Anonymized-lightgrey?style=for-the-badge)](https://github.com/Saxt35/ai-knowledge-platform-graphrag#-nota-de-confidencialidad)

**Autor:** Noe Briones | AI Architect / MDM Lead | HASSERV / COMIMSA
**Repo hermano:** [kyuubi-troubleshooting](https://github.com/Saxt35/kyuubi-troubleshooting)

---
## Nota Confidencialidad
> Anonimizado <HOST> <PORT> <USER> <KYUUBI_HOST> - Metricas reales, artefactos conceptuales

## 1 Objetivo
Busqueda semantica millones registros Oracle/Postgres/MySQL/Excel/PDF + trazabilidad + anti-alucinaciones LLM. Solucion GraphRAG Jena + pgvector + ClickHouse.

## 2 Alcance
Tipo: Diseño Conceptual + PoC | NO es Open Source productivo | Incluye ADRs, diagrama ANON, RAGAS, middleware | Estado faithfulness 0.91 MVP | Proposito CV

## 3 Arquitectura Tecnologias Soporte
[Tecnologias Soporte](./diagrams/tecnologias-soporte-bigdata-platform.png)
[GraphRAG ANON](./diagrams/diagrama_graphrag_ANON.png)

Ingesta Spark-SQL/Mongo/Postgres/Oracle + Kafka Structured Streaming -> OLAP ClickHouse + PostgreSQL + Jena Fuseki + GNN/HUG PyTorch Spark NLP + Tree.js Node.js + Metabase
Infra: HDFS YARN LIVY DOCKER AIRFLOW ZEPPELIN HUE KAFKA - Spark 3.x YARN 4 nodes Kyuubi <KYUUBI_HOST>:10009 - RCA 79.7GB ver kyuubi-troubleshooting

## 4 Participacion Personal
1. Diseño 5 capas 2. ADRs pgvector vs Pinecone->pgvector, ClickHouse vs Druid->ClickHouse, Kyuubi vs Livy->Kyuubi 3. RDF/OWL MDM 4. Middleware Node.js Metabase 5. HDFS HA 6. RAGAS 0.91 GNN/HUG 7. Gobernanza

## 5 Stack
Jena Fuseki pgvector ClickHouse GNN/HUG PyTorch Spark NLP Kafka Next.js Tree.js Metabase HDFS YARN Livy Airflow Zeppelin

## 6 Metricas
Faithfulness 0.91 RAGAS, Hallucinations -40%, Trazabilidad 100% SPARQL, >10M triples

## 7 Estructura
/diagrams/ tecnologias-soporte-bigdata-platform.png + diagrama_graphrag_ANON.png

## 8 Ecosistema
Architecture este repo + Operations kyuubi-troubleshooting RCA 79.7GB /tmp/hive
