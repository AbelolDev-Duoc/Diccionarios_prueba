import os
import csv

validacion_salida = False

def obtener_lista_facturacion():
    datos = {}
    with open('datos.csv', newline='') as archivo:
        lector_csv = csv.DictReader(archivo, delimiter=';')
        for fila in lector_csv:
            año = int(fila['Año'])
            """
            Se crea una lista llamada facturaciones que contiene las 
            facturaciones de los cuatro trimestres. 
            Se usa una lista por comprensión para iterar 
            de 1 a 4 y extraer los valores de los trimestres, 
            convirtiéndolos a float.
            """
            facturaciones = [float(fila[f'Trimestre {i}']) for i in range(1, 5)]
            datos[año] = facturaciones
    return datos

def calcular_media_anual(datos):
    medias = {}
    for año, facturaciones in datos.items():
        media = sum(facturaciones) / len(facturaciones)
        medias[año] = media
    return medias

def imprimir_en_pantalla(medias):
    for año in sorted(medias):
        print(f"Año: {año}, Media de facturación: {medias[año]:.2f}")

def guardar_años_cronologicamente(medias, filename='medias_facturacion.csv'):
    with open(filename, 'w') as csv:
        for año in sorted(medias):
            csv.write(f"Año: {año}, Media de facturación: {medias[año]}\n")

while validacion_salida == False:
    os.system('clear')
    print("Información fiscal")
    print("Seleccione la opción a realizar: ")
    print("1-) Imprimir años con media")
    print("2-) Guardar años cronológicamente")
    print("3-) Salir")
    try:
        opcion = int(input(">>> "))
        match opcion:
            case 1:
                datos = obtener_lista_facturacion()
                medias = calcular_media_anual(datos)
                imprimir_en_pantalla(medias)
                input("Presione ENTER para continuar")
            case 2:
                datos = obtener_lista_facturacion()
                medias = calcular_media_anual(datos)
                guardar_años_cronologicamente(medias)
                print("Datos escritos en 'medias_facturacion.csv'")
                input("Presione ENTER para continuar")
            case 3:
                print("Hasta pronto")
                validacion_salida = True
            case _:
                print("Opción no válida. Intente nuevamente.")
                input("Presione ENTER para continuar")
    except ValueError:
        print("Debe ser un valor numérico.")
        input("Presione ENTER para continuar")
