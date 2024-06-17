# Programa de Facturación Anual

Este programa en Python permite calcular y gestionar datos de facturación anual, proporcionando opciones para visualizar medias de facturación por año y guardar estos datos en un archivo CSV.

## Funcionalidades

- **Obtener Lista de Facturación**: Lee datos desde un archivo CSV (`datos.csv`) que contiene información trimestral de facturación por año.
- **Calcular Media Anual**: Calcula la media de facturación anual para cada año basándose en los datos obtenidos.
- **Imprimir en Pantalla**: Muestra en pantalla la media de facturación para cada año ordenada cronológicamente.
- **Guardar Años Cronológicamente**: Guarda la media de facturación por año en un archivo CSV (`medias_facturacion.csv`) ordenado cronológicamente.
- **Salir**: Permite salir del programa cuando se selecciona esta opción.

## Uso del Programa

El programa presenta un menú interactivo con las siguientes opciones:

1. **Imprimir años con media**: Muestra en pantalla la media de facturación por año.
2. **Guardar años cronológicamente**: Guarda la media de facturación por año en un archivo CSV.
3. **Salir**: Finaliza la ejecución del programa.

## Requisitos

- Python 3.x
- Biblioteca estándar de Python: `os`, `csv`

## Instrucciones de Ejecución

1. Clona el repositorio o descarga el archivo `programa_facturacion.py`.
2. Asegúrate de tener un archivo `datos.csv` en el mismo directorio que contiene la información de facturación trimestral por año.
3. Ejecuta el programa mediante el comando `python programa_facturacion.py`.
4. Sigue las instrucciones en pantalla para utilizar las distintas funcionalidades.

## Ejemplo de Contenido en `datos.csv`

El archivo `datos.csv` debe estar estructurado de la siguiente manera:

