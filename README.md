# Análisis de discurso de los máximos responsables de las empresas participantes del COLCAP

Una aproximación desde modelos clásicos de minería de texto y procesamiento de lenguaje natural. Este repositorio contiene el código y datos para el análisis de las cartas de los máximos responsables de las empresas participantes del COLCAP.

## Objetivos
### Objetivo General
Explorar el uso de técnicas de minería de texto y procesamiento de lenguaje natural para analizar el contenido de las cartas dirigidas por los máximos responsables de empresas colombianas a sus accionistas, identificando patrones y tendencias en el discurso empresarial que sugieran posibles comportamientos en los indicadores bursátiles.

### Objetivos Específicos
- Procesar un conjunto representativo de cartas escritas por los máximos responsables de empresas colombianas listadas en el COLCAP a sus accionistas, utilizando técnicas avanzadas de minería de texto y procesamiento de lenguaje natural.
- Desarrollar métricas que permitan extraer información significativa de las cartas, identificando temas recurrentes, cambios en el discurso a lo largo del tiempo, y cuantificar la polaridad de las expresiones en cada documento.
- Analizar las métricas y patrones identificados en las cartas y su posible influencia en indicadores como el precio de las acciones y la rentabilidad.
- Evaluar la eficacia de las técnicas utilizadas para extraer información de las cartas y su posible impacto en los comportamientos de los indicadores bursátiles.

## Directorios
Este repositorio está organizado en directorios que facilitan la navegación y comprensión de las diversas etapas y componentes del análisis:

### datasets
Contiene los datos brutos y los resultados de los análisis. Se divide en:
- `raw_texts/`: Archivos `.txt` con las cartas de los responsables.
- `results-data/`: Resultados de las métricas y modelos aplicados.
- `supporting_data/`: Datos de apoyo como sectores de empresas y rendimientos históricos.

### notebooks
Notebooks organizados en carpetas que reflejan las etapas del análisis:
#### text-preparation
- [1. Lectura_txt.ipynb](https://github.com/dcuervo1/corporate-text-analysis/edit/main/notebooks/1-Read-text/1.%20Lectura_txt.ipynb): Lectura y procesamiento inicial de los archivos `.txt`.
- [2. PreparaciónTexto.ipynb](notebooks/text-preparation/2.%20PreparaciónTexto.ipynb): Limpieza y preparación de textos para análisis subsiguiente.

#### text-analysis
- [3. Similaridad_Cartas.ipynb](notebooks/text-analysis/3.%20Similaridad_Cartas.ipynb): Análisis de similaridad entre cartas.
- [4. LSA.ipynb](notebooks/text-analysis/4.%20LSA.ipynb): Aplicación de Análisis Semántico Latente.
- [5. AnalisisSentimientos.ipynb](notebooks/text-analysis/5.%20AnalisisSentimientos.ipynb): Análisis de sentimiento de los textos.

#### complementary-processes
- [6. CAPM.ipynb](notebooks/complementary-processes/6.%20CAPM.ipynb): Análisis del modelo CAPM en el mercado.
- [7. Analisis_final.ipynb](notebooks/complementary-processes/7.%20Analisis_final.ipynb): Conclusiones finales del proyecto.
