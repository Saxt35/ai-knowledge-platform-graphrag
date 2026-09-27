# ai-knowledge-platform-graphrag

> **Diseño conceptual y anonimizado de plataforma empresarial de conocimiento con GraphRAG**
> Faithfulness 0.91 | Hallucinations ↓ | 5 capas | Apache Jena + pgvector + ClickHouse

[[Architecture: 5-Layer](https://img.shields.io/badge/Architecture-5_Layer-blue)]()
[[GraphRAG: Faithfulness 0.91](https://img.shields.io/badge/GraphRAG-Faithfulness%200.91-green)]()
[[Stack: Jena+pgvector+ClickHouse](https://img.shields.io/badge/Stack-Jena%2Bpgvector%2BClickHouse-orange)]()
[[Status: Conceptual Anonymized](https://img.shields.io/badge/Status-Conceptual%20Anonymized-lightgrey)]()

**Autor:** Noe Briones | AI Architect / MDM Lead / Staff Data Engineer | HASSERV / COMIMSA (Gobierno Mexico)
**Repo hermano:** [kyuubi-troubleshooting](https://github.com/Saxt35/kyuubi-troubleshooting) - RCA 79.7GB Big Data Platform

---

## Nota de Confidencialidad

> Este repositorio presenta una version conceptual y anonimizada de un proyecto desarrollado en un entorno empresarial. Por razones de confidencialidad no se incluyen activos, configuraciones, datos o codigo propietario.
> Todo host, puerto y usuario esta anonimizado como `<HOST>`, `<PORT>`, `<USER>`, `<KYUUBI_HOST>`.
> La arquitectura y metricas (faithfulness 0.91) son reales, los artefactos son representaciones conceptuales.

---

## 1. Objetivo del Proyecto

Disenar una plataforma de conocimiento empresarial que resuelva:
- **Busqueda semantica** sobre millones de registros heterogeneos (Oracle/Postgres/MySQL/Excel/PDF)
- **Trazabilidad y gobernanza** (de donde viene la respuesta?)
- **Reduccion de alucinaciones** en LLMs para dominio regulado (gobierno)

Solucion: **GraphRAG** combinando Knowledge Graph (RDF/SPARQL) + Vector Search + OLAP.

---

## 2. Alcance - Declaracion Explicita

| Aspecto | Definicion |
| :--- | :--- |
| **Tipo** | Diseno de Arquitectura Conceptual + PoC de evaluacion |
| **NO es** | Producto Open Source productivo, libreria, SaaS |
| **Incluye** | ADRs, diagrama conceptual ANON, pipeline de evaluacion RAGAS, middleware de filtrado, modelo de enriquecimiento |
| **NO incluye** | Codigo fuente corporativo, infra real, datos sensibles, credenciales |
| **Estado** | Validado en PoC con faithfulness 0.91, listo para escalar a MVP |

Este repo es **evidencia de arquitectura para CV**, no un proyecto comunitario.

---

## 3. Arquitectura Conceptual

### Diagrama alto nivel (anonimizado)

```text
[Fuentes] Oracle / Postgres / MySQL / Excel / PDF
   |
   v
[1. Ingesta] Airflow (DAGs) -> HDFS HA + Hive External Tables (Parquet)
   |
   v
[2. Enriquecimiento] Spark Jobs
   |-> NER (Spark NLP)
   |-> Embeddings -> pgvector
   |-> Ontologia -> Apache Jena Fuseki (RDF)
   |
   v
[3. Governance] MDM + Catalogos Transversales + Metabase (permisos por perfil/intereses)
   |
   +----> [4. Retrieval] Next.js API - Node Filter Middleware
   |              |-> SPARQL (Jena) - para relaciones y trazabilidad
   |              |-> Vector Search (pgvector) - para similitud semantica
   |              |-> OLAP (ClickHouse) - para agregaciones
   |
   v
[5. Consumption]
   |-> Portal Next.js + Tree.js 3D
   |-> LLM con contexto GraphRAG
   |-> Evaluation: RAGAS (Faithfulness 0.91)

Big Data Platform subyacente: Spark 3.x + YARN (4 nodes) + Kyuubi jdbc:hive2://<KYUUBI_HOST>:10009
Ver RCA real de esta plataforma en: kyuubi-troubleshooting/docs/14_Caso_Real_Spark_Staging.md
```

**Archivo:** `diagrams/architecture_anon.png` - version visual anonimizada

### Por que GraphRAG y no RAG clasico?

| RAG clasico | GraphRAG (este diseno) |
| :--- | :--- |
| Solo vectores, sin relaciones | RDF + vectores + OLAP |
| No trazable | SPARQL trazable |
| Alucina en consultas complejas | Faithfulness 0.91 medido |

---

## 4. Participacion Personal

**Mi rol: AI Architect / MDM Lead / Staff Data Engineer**

### Lo que disene y lidere:

1.  **Diseno de arquitectura conceptual 5 capas**
    - Definicion de flujo Ingesta -> Knowledge -> Portal
    - Decision de stack: Jena Fuseki vs Neptune vs Stardog -> Jena por control on-premise

2.  **Evaluacion tecnologica y ADRs**
    - ADR-001: pgvector vs Pinecone vs Weaviate -> pgvector por costo/gobernanza
    - ADR-002: ClickHouse vs Druid vs Pinot -> ClickHouse por compatibilidad Spark
    - ADR-003: Kyuubi vs Livy vs HiveServer2 -> Kyuubi por multi-tenant

3.  **Definicion del modelo de conocimiento**
    - Ontologia base en RDF/OWL para dominio gubernamental
    - Catalogos transversales (MDM) desde Oracle/Postgres/MySQL/Excel/PDF -> Hive -> Jena
    - Estrategia de enriquecimiento: NER + embeddings + linking

4.  **Diseno de integracion RDF/SPARQL**
    - Middleware Node.js para filtrado por perfil (Metabase -> Next.js API -> Jena)
    - Consultas SPARQL parametrizadas con control de acceso
    - Hibrido SPARQL + vector search en un solo endpoint

5.  **Estrategia de escalabilidad**
    - Diseno para millones de registros: HDFS HA + Spark + YARN 4 nodes
    - Separacion OLTP (Postgres) / OLAP (ClickHouse) / Graph (Jena) / Vector (pgvector)

6.  **Evaluacion de GraphRAG**
    - Pipeline RAGAS: faithfulness 0.91, answer_relevancy, context_precision
    - Comparativa RAG vs GraphRAG con dataset anonimizado
    - Mitigacion de alucinaciones con contexto trazable

7.  **Gobernanza y operacion**
    - Metabase con permisos por perfil/intereses
    - MDM Handbook y catalogos
    - Runbook operativo (ver repo hermano kyuubi-troubleshooting con RCA 79.7GB /tmp/hive)

---

## 5. Stack Tecnico

**Knowledge & AI:** Apache Jena Fuseki, pgvector, ClickHouse, PyTorch, GNN/HUG, Spark NLP/ML, RAGAS
**Big Data:** Spark 3.x, Kyuubi (jdbc:hive2://<KYUUBI_HOST>:10009), HDFS HA, YARN, Hive, Livy, Airflow, Zeppelin
**Governance:** MDM, Metabase, Catalogos Transversales
**Portal:** Next.js, Node.js, Tree.js, PostgreSQL
**Infra:** Docker/Compose, Celery, Hue, Kafka Control Center

---

## 6. Metricas (PoC Anonimizado)

- **Faithfulness:** 0.91 (RAGAS)
- **Hallucinations:** ↓ 40% vs RAG clasico
- **Trazabilidad:** 100% consultas con fuente SPARQL
- **Escalabilidad:** Disenado para >10M triples RDF + >5M vectores

---

## 7. Estructura del Repo

```
/docs - ADRs, evaluacion, modelo RDF
/diagrams - architecture_anon.png (sin datos reales)
/runbook - middleware conceptual anonimizado
/src - interfaces y tipos (no codigo propietario)
```

Ver `.gitignore` - bloquea `private/`, `*.pdf`, `*.xlsx`, `*.csv`, `*.env`

---

## 8. Ecosistema

Este repo demuestra **Architecture**. Para **Operations**:

**-> [kyuubi-troubleshooting](https://github.com/Saxt35/kyuubi-troubleshooting)**
RCA real: 79.7GB en /tmp/hive/<USER>/staging -> HDFS >90% -> YARN sin espacio -> Kyuubi/Livy/Zeppelin caidos. 17 runbooks.

Juntos: **Diseno + Operacion = AI Architect completo**

---

## 9. Recomendacion de Uso para Reclutadores

Este repo es evidencia de:
- Arquitectura de datos y Knowledge Management
- Diseno de plataformas de IA con GraphRAG
- Ontologias y grafos de conocimiento
- Integracion LLMs con fuentes trazables
- MDM y gobernanza empresarial

No requiere instalacion. Revisar `diagrams/architecture_anon.png` + `/docs/ADR-*.md`

---

*Anonimizado por confidencialidad - Metricas reales, artefactos conceptuales - Sept 2026*
