import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def run_notebook(path):
    with open(path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': os.path.dirname(path)}})

    print(f"Ejecutado: {path}")

# Obtén el directorio del script actual
current_dir = os.path.dirname(os.path.abspath(__file__))

notebooks = [
    "1.Lectura_txt.ipynb",
    "2.PreparaciónTexto.ipynb",
    "3.Similaridad_Cartas.ipynb",
    "4.LSA.ipynb",
    "5.AnalisisSentimientos.ipynb",
    "6.CAPM.ipynb",
    "7.Analisis_complementario.ipynb"
]

print("Archivos .ipynb en el directorio:")
for file in os.listdir(current_dir):
    if file.endswith('.ipynb'):
        print(file)

print("\nEjecutando notebooks:")
for notebook in notebooks:
    notebook_path = os.path.join(current_dir, notebook)
    if os.path.exists(notebook_path):
        try:
            run_notebook(notebook_path)
        except Exception as e:
            print(f"Error al ejecutar {notebook}: {str(e)}")
    else:
        print(f"Archivo no encontrado: {notebook}")