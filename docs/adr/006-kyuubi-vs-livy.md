# ADR-006: Kyuubi vs Livy
Date: 2025-08-25 | Status: Accepted
Diagrama: APACHE LIVY + jdbc:hive2://<KYUUBI_HOST>:10009 + YARN
Evidencia: kyuubi-troubleshooting RCA 79.7GB /tmp/hive/<USER>/staging

Decisión: Kyuubi principal, Livy fallback.

Justificación (RCA real):
- Livy dejaba /tmp/hive/<USER>/staging sin limpiar -> HDFS >90% -> YARN sin espacio -> Zeppelin caído
- Kyuubi limpia staging al cerrar sesión + <USER> isolation + YARN queues
- Zeppelin/Hue conectan a jdbc:hive2://<KYUUBI_HOST>:10009 (bloque HUE+ZEPPELIN), Livy solo REST
- Kyuubi HA con ZooKeeper

Consecuencias: +HDFS <70% estable, +0 caídas Zeppelin.