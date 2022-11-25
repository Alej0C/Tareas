import csv


def menu():
    print("*" * 45)
    print("\t1. Llenar la lista")
    print("\t2. Crear el archivo csv")
    print("\t3. Actualizar el archivo csv")
    print("\t4. eliminar un dato")
    print("\t5. Salir")
    print("*" * 45)


def llenar(vector, cnt_personas):
    for i in range(cnt_personas):
        vector.append([])
        for j in range(3):
            dato = str(input("Digite el " + vector[0][j] + " de la persona: "))
            vector[i + 1].append(dato)


def creando(lista_datos):  #Función crear archivo csv
    ubicacion_csv = "C:\\Users\\ACER\\OneDrive\\Escritorio\\Datos.csv"
    with open(
            ubicacion_csv, 'w', newline=''
    ) as csvfile:  #with open permite abrir el archivo y crearlo con la sentencia 'w'4
        writer = csv.writer(
            csvfile, delimiter=';'
        )  #el objeto csv.writer permite dar los parámetros de como debe ser creado el archivo plano
        writer.writerows(
            lista_datos
        )  #el objeto writerows me permite escribir toda la lista en líneas separadas


def leyendo():  #Función leer archivo csv
    ubicacion_csv = "C:\\Users\\ACER\\OneDrive\\Escritorio\\Datos.csv"
    with open(
            ubicacion_csv, 'r', newline=''
    ) as csvfile:  #with open permite abrir el archivo y leerlo por medio de la sentencia 'r'
        reader = csv.reader(
            csvfile, delimiter=';'
        )  #el objeto csv.reader permite leer el archivo por medio de los parametro dados
        for row in reader:  #Me permite hacer el recorrido del archivo plano para imprimirlo en pantalla
            print(row)  #Imprime la lista línea por línea


def agregando(ubicacion_csv,
              lista_datos2):  #Función agregar al final del archivo csv
    with open(
            ubicacion_csv, 'r', newline=''
    ) as csvfile:  #with open permite abrir el archivo y leerlo por medio de la sentencia 'r'
        reader = csv.reader(
            csvfile, delimiter=';'
        )  #el objeto csv.reader permite leer el archivo por medio de los parametro dados
        data = [
            line for line in reader
        ]  #La variable data cumple la función de una lista, la cual recibe los datos del csv y los almacena
    with open(
            ubicacion_csv, 'w', newline=''
    ) as csvfile:  #with open permite abrir el archivo y crearlo con la sentencia 'w'
        writer = csv.writer(
            csvfile, delimiter=';'
        )  #el objeto csv.writer permite dar los parámetros de como debe ser creado el archivo plano
        writer.writerows(data)  #Escribo los datos que contenia el csv de nuevo
        writer.writerows(
            lista_datos2
        )  #Escribo en el archivo csv los datos de la lista a agregar


def eliminando(
    search
):  #Funcion eliminar, esta elimina la línea que se entrega por parámetro
    ubicacion_csv = "C:\\Users\\ACER\\OneDrive\\Escritorio\\Datos.csv"
    with open(
            ubicacion_csv, 'r', newline=''
    ) as csvfile:  #with open permite abrir el archivo y leerlo por medio de la sentencia 'r'
        reader = csv.reader(
            csvfile, delimiter=';'
        )  #el objeto csv.reader permite leer el archivo por medio de los parametro dados
        data = [
            line for line in reader
        ]  #La variable data cumple la función de una lista, la cual recibe los datos del csv y los almacena
    with open(
            ubicacion_csv, 'w', newline=''
    ) as csvfile:  #with open permite abrir el archivo y crearlo con la sentencia 'w'
        writer = csv.writer(
            csvfile, delimiter=';'
        )  #el objeto csv.writer permite dar los parámetros de como debe ser creado el archivo plano
        data.pop(
            search
        )  #llamando a la lista data se elimina la linea dada utilizando la función pop
        writer.writerows(
            data)  #Escribo los datos que contiene la lista modificada.


def main():
    vector = [['Id', 'Nombre', 'Apellido']]
    continuar = True
    submenu = True

    while continuar:
        menu()
        opt = int(input("Seleccione una opcion: "))
        if opt == 1:
            cnt_personas = int(input("Cantidad de personas: "))
            llenar(vector, cnt_personas)
            print(vector)
            creando(vector)
        elif opt == 2:
            leyendo()
        elif opt == 3:
            print("\t1. Agregar")
            print("\t2. Eliminar")
            op = int(input("Seleccione una opcion: "))
            if (op >= 1 and op <= 2):
                if op == 1:
                    op = int(input("Que desea agregar: "))
                    ubicacion = "C:\\Users\\ACER\\OneDrive\\Escritorio\\Datos.csv"
                    vector2 = [['2', 'Juan', 'Gomez'], ['3', 'Jesus', 'Perez']]
                    agregando(ubicacion, vector2)
            elif op == 2:
                op = int(input("Que valor desea eliminar: "))
                eliminando(op)
            else:
                print("Opcion no encontrada")
        elif opt == 4:
            op = int(input("Que elemento desea eliminar: "))
            eliminando(op)
        elif opt == 5:
            print("\nSaliendo del menu")
            continuar = False
        else:
            print("\nOpción no encotrada")


main()