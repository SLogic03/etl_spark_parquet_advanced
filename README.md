# ETL Spark Parquet Advanced

Repositorio base para el proyecto de ETL con datos Parquet y capas Bronze, Silver y Gold.

## Estructura

- `data/raw/`: archivos fuente por tipo y partición temporal.
- `data/bronze/`, `data/silver/`, `data/gold/`: zonas de procesamiento.
- `data/quarantine/`: registros rechazados o inválidos.
- `data/audit/`: trazabilidad y control de calidad.
- `metadata/`: esquemas esperados y reglas de negocio.
- `notebooks/`: flujo de trabajo del proyecto.
- `src/`: lógica reutilizable en Python.
- `config/`: configuración del ETL.

> Nota: los archivos `.parquet` creados aquí son marcadores de posición para la estructura del repositorio.
