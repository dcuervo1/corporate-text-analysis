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

## Directorios dentro de carpeta Tesis
Este repositorio está organizado en directorios que facilitan la navegación y comprensión de las diversas etapas y componentes del análisis:

### 1.0.Source
Contiene los datos crudos y de soporte de los análisis. Se divide en:
- `Colcap_DataText/`: Archivos `.txt` con cada una de las cartas de los responsables.
- `Contexto/`: Datos de apoyo como sectores de empresas y rendimientos históricos.
### 1.1.Output
Se almacenan los resultados de cada notebook:
- `1.1.Output/`: Resultados de las métricas y modelos aplicados en único archivo `.csv`.

## notebooks dentro de carpeta Tesis
Notebooks organizados que reflejan las etapas del análisis, el primer archivo es un `.py` que ejecuta todos los notebooks, en este se encuentra la versión de python que se requiere para la ejecución de estos notebooks de forma adecuada, tambien se pueden ejecutar en orden cada archivo `.ipynb`, con el fin de verificar si las librerias y dependencias se encuentran en el entorno de ejecución actual.

- [0. Run_Notebooks](https://github.com/dcuervo1/corporate-text-analysis/blob/main/Tesis/0.Run_Notebooks.py): Script `.py` para la ejecución de los notebooks.
- [1. Lectura_txt.ipynb](https://github.com/dcuervo1/corporate-text-analysis/blob/main/Tesis/1.Lectura_txt.ipynb): Lectura y procesamiento inicial de los archivos `.txt`.
- [2. PreparaciónTexto.ipynb](https://github.com/dcuervo1/corporate-text-analysis/blob/main/Tesis/2.PreparaciónTexto.ipynb): Limpieza y preparación de textos para análisis subsiguiente.
- [3. Similaridad_Cartas.ipynb](https://github.com/dcuervo1/corporate-text-analysis/blob/main/Tesis/3.Similaridad_Cartas.ipynb): Análisis de similaridad entre cartas.
- [4. LSA.ipynb](https://github.com/dcuervo1/corporate-text-analysis/blob/main/Tesis/4.LSA.ipynb): Aplicación de Análisis Semántico Latente.
- [5. AnalisisSentimientos.ipynb](https://github.com/dcuervo1/corporate-text-analysis/blob/main/Tesis/5.AnalisisSentimientos.ipynb): Análisis de sentimiento de los textos.

### Proceso complementario de análisis
- [6. CAPM.ipynb](https://github.com/dcuervo1/corporate-text-analysis/blob/main/Tesis/6.CAPM.ipynb): Análisis del modelo CAPM (Capital Asset Pricing Model) en el índice de referencia COLCAP.
- [7. Analisis_complementario.ipynb](https://github.com/dcuervo1/corporate-text-analysis/blob/main/Tesis/7.Analisis_complementario.ipynb): Analisis de exploración y soporte de resultados.

- [Dashboard análisis de discurso de cartas de máximos responsables.](https://app.powerbi.com/view?r=eyJrIjoiM2Q0ZGRlYzgtMTFiNC00OGIyLThjYzEtNmJlNDE4OWQxNjEwIiwidCI6IjI3MWRmNTg0LWFiNjQtNDM3Zi04NWI2LTgwZmY5YmVmNmM5ZiIsImMiOjZ9): Para una visualización interactiva de los resultados, visita el dashboard de análisis de métricas obtenidas en el trabajo.
