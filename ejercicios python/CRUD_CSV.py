import csv


def menu_principal():
    print("*" * 45)
    print("\t1. Crear csv")
    print("\t2. Lectura de archivo csv")
    print("\t3. Actualizar archivo csv")
    print("\t4. Buscar y eliminar un dato")
    print("\t5. Salir")
    print("*" * 45)


def llenar(vector, cnt_personas):
    for i in range(cnt_personas):
        vector.append([])
        for j in range(3):
            dato = str(input("Digite el " + vector[0][j] + " de la persona: "))
            vector[i + 1].append(dato)


def creando(ubicacion_csv, lista_datos):  #Función crear archivo csv
    with open(
            ubicacion_csv, 'w', newline=''
    ) as csvfile:  #with open permite abrir el archivo y crearlo con la sentencia 'w'
        writer = csv.writer(
            csvfile, delimiter=';'
        )  #el objeto csv.writer permite dar los parámetros de como debe ser creado el archivo plano
        writer.writerows(
            lista_datos
        )  #el objeto writerows me permite escribir toda la lista en líneas separadas


def leyendo(ubicacion_csv):  #Función leer archivo csv
    with open(
            ubicacion_csv, 'r', newline=''
    ) as csvfile:  #with open permite abrir el archivo y leerlo por medio de la sentencia 'r'
        reader = csv.reader(
            csvfile, delimiter=';'
        )  #el objeto csv.reader permite leer el archivo por medio de los parametro dados
        for row in reader:  #Me permite hacer el recorrido del archivo plano para imprimirlo en pantalla
            print(row)  #Imprime la lista línea por línea


def agregando(ubicacion_csv,
              lista_datos):  #Función agregar al final del archivo csv
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
            lista_datos
        )  #Escribo en el archivo csv los datos de la lista a agregar


def eliminando(
    search, ubicacion_csv
):  #Funcion eliminar, esta elimina la línea que se entrega por parámetro
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


#guardar la lista anterior para actualizar el documento, consultar ¿Cómo retornar una lista en python?

vector = []
cnt_personas = []
ubicacion_csv = []
lista_datos = [['id', 'nombre', 'apellido']]
search = []


def main():
    continuar = True
    submenu = True

    while continuar:
        menu_principal()
        opt = int(input("Seleccione una opción: "))
        if opt == 1:
            op = int(
                input(
                    "Ingrese el tamaño de la lista, 2 para salir al menu principal\n"
                ))
            llenar(lista_datos, op)
            val_op = 2
            if op == 1:
                while val_op != op:
                    op = int(
                        input(
                            "Presione 1 para crear archivo csv, 2 para salir al menú principal\n"
                        ))
                    creando(ubicacion_csv, lista_datos)
            else:
                print("Opcion no encontrada")
        elif opt == 2:
            print("Lectura del archivo csv\n")
            leyendo(ubicacion_csv)
        if opt == 3:
            print("Que desea actulizar en el archivo csv\n")
            op = int(
                input(
                    "Que elemento desea añadir, 2 para salir al menu principal\n"
                ))
            agregando(ubicacion_csv, lista_datos)
            val_op = 2
            if op == 3:
                while val_op != 0:
                    op = int(
                        input(
                            "Que elemento desea eliminar, 2 para salir al menu principal\n"
                        ))
                    eliminando(search, ubicacion_csv)
        elif opt == 5:
            print("\nSaliendo del menu")
            continuar = False
        else:
            print("\nOpción no encotrada")


main()