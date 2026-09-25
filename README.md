# ai-knowledge-platform-graphrag

Plataforma de conocimiento GraphRAG lista para producción, diseñada para millones de documentos con trazabilidad end-to-end.

## Arquitectura

- **Knowledge Graphs** con **RDF/SPARQL** y **Apache Jena**
- **Hybrid Retrieval** con búsqueda **vectorial + grafo + re-ranker**
- **LLMs** con **LangChain** y **OpenAI**
- Stack distribuido con **Spark, PySpark, Airflow, Zeppelin, Livy, Kyuubi, ClickHouse, Hive** y despliegue en **Azure K8s**

## Enfoque

- Baja alucinación con objetivo de **faithfulness > 0.9**
- Gobierno de datos, trazabilidad y lineage
- Aplicable a sectores **financiero, industrial y de investigación pública**
- Casos de referencia: **HASSERV** y **COMIMSA/CONACyT**
