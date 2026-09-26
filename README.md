# AI Knowledge Platform - GraphRAG Architecture

> Plataforma de conocimiento con GraphRAG diseñada en HASSERV y COMIMSA/CONACyT para millones de registros con trazabilidad y baja alucinación.

**Author:** Noé Briones Pérez - AI Architect | Solution Architect - Generative AI & Data
**Experiencia aplicada:** HASSERV (Sector Financiero e Industrial), COMIMSA/CONACyT (Institución pública de investigación), Grupo Aura / IPICYT (Sector Industrial)
**Stack:** Spark, PySpark, Apache Jena, RDF/SPARQL, LangChain, OpenAI, ClickHouse, Hive, Airflow, Zeppelin, Livy, Kyuubi, Azure K8s, Java 17, Spring 6

---

### Arquitectura

[Architecture](./docs/architecture.png)

### Objetivo
Transformar datos dispersos y no estructurados (PDFs, bases de datos heterogéneas Oracle/PostgreSQL, documentos técnicos de COMIMSA y sector financiero) en una capa de conocimiento consultable en lenguaje natural, con citas trazables y sin alucinaciones.

### Flujo aplicado en proyectos reales

**1. Data Sources - HASSERV / COMIMSA**
- 10M+ documentos, PDFs, bases Oracle/PG, APIs de sistemas institucionales

**2. Ingestion**
- Apache Airflow para orquestación
- PySpark Jobs vía Zeppelin, Livy, Kyuubi (stack usado en HASSERV)

**3. Enrichment**
- Chunking semántico 500 tokens con overlap
- Embeddings OpenAI
- Extracción de entidades y relaciones (NER)
- Modelado de ontología RDF

**4. Knowledge Build**
- Apache Jena TDB
- RDF / SPARQL
- Entidades modeladas en proyectos: Empresa, Persona, Riesgo, Documento, Proceso

**5. Storage Híbrido**
- 5a. Vector Store: FAISS / Azure AI Search
- 5b. Graph Store: Jena Graph DB - SPARQL + Inferencia + Linaje y gobierno de datos (diseño para COMIMSA)
- 5c. Analytical Store: ClickHouse + Hive - OLAP, métricas de uso y costos (implementado en Grupo Aura)

**6. Hybrid Retrieval**
- Retriever híbrido: Vector + Graph
- Re-ranker + SPARQL Validator

**7. LLM Orchestration**
- LangChain + OpenAI LLM
- Prompts con citas obligatorias de nodos RDF
- Guardrails + PII Masking + MCP Context Manager

**8. Evaluation & Ops**
- Métricas: Faithfulness >0.9, Answer Relevance, Context Precision
- OpenTelemetry, Azure K8s + OpenShift, Jenkins CI/CD (experiencia COMIMSA/HASSERV)

**9. Serving Layer**
- REST API Spring 6 / Java 17 (modernización liderada en COMIMSA)
- Chat UI con citas trazables
- RBAC + Audit Trail

---

### Proyectos donde se aplicó

- **HASSERV (2024-Actual) | Solution Architect:** Diseño de plataforma GraphRAG + Web Semántica para explotación de conocimiento en sector financiero e industrial.
- **COMIMSA / CONACyT (2021-2024) | Solution Architect Transformación Digital:** Consolidación de +10 sistemas heterogéneos en modelo integral y base para arquitectura de conocimiento.
- **Grupo Aura / IPICYT (2017-2021):** Big Data Analytics con Hive + ClickHouse.

### Por qué GraphRAG vs RAG puro

RAG vectorial puro funciona para FAQ. En mis proyectos financieros e industriales con relaciones complejas (cliente-empresa-riesgo-documento), el vector solo alucina. GraphRAG con Jena/RDF aporta razonamiento multi-salto y trazabilidad completa.

### Métricas objetivo

- Faithfulness > 0.9
- Latencia p95 < 2s
- Reducción costo tokens 40% con cache semántico

### Stack completo

Java 17, Spring Boot 3 / Spring 6, Jakarta EE, Spark, PySpark, Apache Jena, RDF, SPARQL, LangChain, OpenAI, ClickHouse, Hive, Airflow, Azure, Docker, Kubernetes, OpenShift, Jenkins, PostgreSQL, Oracle
