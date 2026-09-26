# ADR 001: Por qué RDF/SPARQL (Apache Jena) vs Neo4j

Fecha: 2026-09-25
Autor: Noé Briones Pérez - AI Architect
Contexto: HASSERV / COMIMSA

## Contexto
Necesitábamos Knowledge Graph para sector financiero e industrial con requisitos de gobierno de datos, interoperabilidad y razonamiento semántico.

## Decisión
Elegir Apache Jena TDB + RDF/SPARQL en lugar de Neo4j.

## Razones
- Estándar W3C, interoperable con ontologías existentes
- SPARQL + inferencia (RDFS/OWL) para linaje
- Mejor para auditoría y trazabilidad requerida por cliente
- Integración natural con pipelines Java 17 / Spring 6

## Consecuencias
- Pros: Gobierno, trazabilidad, estándar
- Contras: Traversal menos performante que Neo4j para fraude en tiempo real

## Alternativa futura
Para casos de fraude real-time <100ms, evaluar Neo4j como Graph Store secundario.