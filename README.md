# ai-knowledge-platform-graphrag

> **Diseño conceptual y anonimizado de plataforma empresarial de conocimiento con GraphRAG**
> Faithfulness 0.91 | Hallucinations ↓ | 5 capas | Apache Jena + pgvector + ClickHouse

[![Architecture: 5-Layer](https://img.shields.io/badge/Architecture-5_Layer-blue?style=for-the-badge)](https://github.com/Saxt35/ai-knowledge-platform-graphrag#3-arquitectura-conceptual---tecnologías-soporte)
[![GraphRAG: Faithfulness 0.91](https://img.shields.io/badge/GraphRAG-Faithfulness%200.91-green?style=for-the-badge)](https://github.com/Saxt35/ai-knowledge-platform-graphrag#6-métricas-poc)
[![Stack: Jena+pgvector+ClickHouse](https://img.shields.io/badge/Stack-Jena%2Bpgvector%2BClickHouse-orange?style=for-the-badge)](https://github.com/Saxt35/ai-knowledge-platform-graphrag#5-stack-técnico-mapeado-al-diagrama)
[![Status: Conceptual Anonymized](https://img.shields.io/badge/Status-Conceptual%20Anonymized-lightgrey?style=for-the-badge)](https://github.com/Saxt35/ai-knowledge-platform-graphrag#-nota-de-confidencialidad)

**Autor:** Noe Briones | AI Architect / MDM Lead / Staff Data Engineer | HASSERV / COMIMSA
**Repo hermano:** [kyuubi-troubleshooting](https://github.com/Saxt35/kyuubi-troubleshooting) - RCA 79.7GB Big Data Platform

---

## ⚠️ Nota de Confidencialidad

> Este repositorio presenta una versión conceptual y anonimizada de un proyecto desarrollado en un entorno empresarial. Por razones de confidencialidad no se incluyen activos, configuraciones, datos o código propietario.
> Todo host, puerto y usuario está anonimizado como `<HOST>`, `<PORT>`, `<USER>`, `<KYUUBI_HOST>`.
> La arquitectura y métricas (faithfulness 0.91) son reales, los artefactos son representaciones conceptuales.

---

## 1. Objetivo del Proyecto

Diseñar una plataforma de conocimiento empresarial que resuelva:
- **Búsqueda semántica** sobre millones de registros heterogéneos (Oracle/Postgres/MySQL/Excel/PDF)
- **Trazabilidad y gobernanza** (¿de dónde viene la respuesta?)
- **Reducción de alucinaciones** en LLMs para dominio regulado (gobierno)

Solución: **GraphRAG** combinando Knowledge Graph (RDF/SPARQL) + Vector Search + OLAP.

---

## 2. Alcance - Declaración Explícita

| Aspecto | Definición |
| :--- | :--- |
| **Tipo** | Diseño de Arquitectura Conceptual + PoC de evaluación |
| **NO es** | Producto Open Source productivo, librería, SaaS |
| **Incluye** | ADRs, diagrama conceptual ANON, pipeline de evaluación RAGAS, middleware de filtrado, modelo de enriquecimiento |
| **NO incluye** | Código fuente corporativo, infra real, datos sensibles, credenciales |
| **Estado** | Validado en PoC con faithfulness 0.91, listo para escalar a MVP |

Este repo es **evidencia de arquitectura para CV**, no un proyecto comunitario.

---

## 3. Arquitectura Conceptual - Tecnologías Soporte

### Diagrama 1: Tecnologías Soporte - Big Data Platform

Este diagrama responde al punto #2 de la auditoría "Falta una arquitectura conceptual":

[Tecnologias Soporte - Big Data Platform](./diagrams/tecnologias-soporte-bigdata-platform.png)

**Ubicación:** `diagrams/tecnologias-soporte-bigdata-platform.png`

**Lectura por capas (mapeado a badges):**

- **Badge Architecture: 5-Layer** -> 5 capas visibles:
  - **Ingesta:** Spark-SQL / MongoDB / Postgres / Oracle + Apache Kafka (Spark Structured Streaming)
  - **Storage OLAP:** OLAP ClickHouse
  - **Storage Vector:** PostgreSQL + pgvector
  - **Storage Graph:** Apache Jena Fuseki database
  - **AI Enrichment:** GNN / HUG Geometric deep learning / PYTorch / Spark NLP / Spark ML
  - **Consumption:** JavaScript Node.js Tree.js 3D model + Metabase

- **Infrastructure & Tools (barra inferior del diagrama):**
  HADOOP HDFS - HADOOP YARN - APACHE LIVY - DOCKER - DOCKER COMPOSE - CELERY - APACHE AIRFLOW - APACHE ZEPPELIN - HUE - KAFKA CONTROL CENTER - KAFKA CONNECT
  Subyacente: Spark 3.x + YARN 4 nodes + Kyuubi jdbc:hive2://<KYUUBI_HOST>:10009
  Ver RCA real de esta plataforma: [kyuubi-troubleshooting/docs/14_Caso_Real_Spark_Staging.md](https://github.com/Saxt35/kyuubi-troubleshooting/blob/main/docs/14_Caso_Real_Spark_Staging.md) - 79.7GB /tmp/hive/<USER>/staging

### Diagrama 2: GraphRAG ANON

[GraphRAG ANON](./diagrams/diagrama_graphrag_ANON.png)

Flujo detallado GraphRAG: Documentos -> Extracción Entidades -> Knowledge Graph RDF -> SPARQL + Vector Search -> LLM

### Flujo texto (complemento a ambos diagramas):

```text
[Fuentes Oracle/Postgres/MySQL/Excel/PDF]
  v
[Airflow DAGs] -> HDFS HA + Hive External Tables
  v
[Spark Jobs + Kafka Structured Streaming]
  |-> NER (Spark NLP) -> pgvector
  |-> Embeddings -> pgvector
  |-> Ontología -> Apache Jena Fuseki RDF
  |
  v
[Governance] MDM + Catálogos Transversales + Metabase
  |
  +----> [Retrieval] Next.js API Node Filter Middleware
  |              |-> SPARQL Jena - relaciones y trazabilidad
  |              |-> Vector Search pgvector - similitud
  |              |-> OLAP ClickHouse - agregaciones
  |
  v
[Consumption] Portal Next.js + Tree.js 3D + LLM + RAGAS 0.91
```

---

## 4. Participación Personal

**Rol: AI Architect / MDM Lead**

1. **Diseño arquitectura 5 capas** - Flujo Ingesta -> Knowledge -> Portal (ver Diagrama 1)
2. **Evaluación tecnológica ADRs:**
   - ADR-001: pgvector vs Pinecone -> pgvector (costo/gobernanza) - ver PostgreSQL en diagrama
   - ADR-002: ClickHouse vs Druid -> ClickHouse (compatibilidad Spark) - ver OLAP ClickHouse en diagrama
   - ADR-003: Kyuubi vs Livy -> Kyuubi multi-tenant - ver Infrastructure & Tools
3. **Modelo conocimiento RDF/OWL** - MDM desde Oracle/Postgres/MySQL/Excel/PDF -> Hive -> Jena Fuseki
4. **Integración RDF/SPARQL** - Middleware Node.js filtrado por perfil Metabase -> Next.js API -> Jena Fuseki
5. **Escalabilidad** - HDFS HA + Spark + YARN 4 nodes, separación OLTP/OLAP/Graph/Vector
6. **Evaluación GraphRAG** - RAGAS faithfulness 0.91, GNN/HUG PyTorch Spark NLP
7. **Gobernanza** - Metabase permisos, MDM Handbook, Runbook operativo (ver repo hermano RCA 79.7GB)

---

## 5. Stack Técnico (mapeado al diagrama)

**Del diagrama Tecnologías Soporte (Badge Stack: Jena+pgvector+ClickHouse):**
- Ingesta: Spark-SQL, MongoDB, Postgres, Oracle, Apache Kafka Spark Structured Streaming
- Storage: OLAP ClickHouse, PostgreSQL, Apache Jena Fuseki database
- AI: GNN/HUG Geometric deep learning PYTorch Spark NLP Spark ML
- Portal: JavaScript Node.js Tree.js 3D model
- Consumo: Metabase
- Infra: Hadoop HDFS, Hadoop YARN, Apache Livy, Docker, Docker Compose, Celery, Apache Airflow, Apache Zeppelin, Hue, Kafka Control Center, Kafka Connect

**Adicional GraphRAG (Badge GraphRAG: Faithfulness 0.91):** pgvector, PyTorch, RAGAS 0.91

---

## 6. Métricas PoC

- **Faithfulness:** 0.91 (RAGAS) - ver Badge GraphRAG
- **Hallucinations:** ↓ 40% vs RAG clásico
- **Trazabilidad:** 100% consultas con fuente SPARQL Jena
- **Escalabilidad:** >10M triples RDF + >5M vectores

---

## 7. Estructura Repo

```
/diagrams/
  - tecnologias-soporte-bigdata-platform.png <- Diagrama 1 (Tecnologías Soporte)
  - diagrama_graphrag_ANON.png <- Diagrama 2 (GraphRAG)
/docs/ - ADRs, evaluación, modelo RDF
/runbook/ - middleware conceptual anonimizado
```

.gitignore bloquea private/, *.pdf, *.xlsx, *.csv, *.env

---

## 8. Ecosistema

**Architecture (este repo)** -> Diagrama Tecnologías Soporte + GraphRAG ANON
**Operations:** [kyuubi-troubleshooting](https://github.com/Saxt35/kyuubi-troubleshooting) - RCA 79.7GB /tmp/hive/<USER>/staging -> HDFS >90% -> YARN sin espacio -> Kyuubi/Livy/Zeppelin caídos, 17 runbooks

Juntos: Diseño + Operación = AI Architect completo

---

## 9. Para Reclutadores

Evidencia de: Arquitectura datos, Knowledge Management, Plataformas IA GraphRAG, Ontologías grafos conocimiento, Integración LLMs trazables, MDM gobernanza empresarial, Big Data Platform (Spark, YARN, HDFS, Kyuubi, Kafka, ClickHouse, Jena)

No requiere instalación. Revisar diagramas en `/diagrams` + docs/ADR-*.md

*Anonimizado - Métricas reales, artefactos conceptuales - Sept 2026*
