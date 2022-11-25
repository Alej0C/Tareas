import csv

def llenar(vector, cnt_personas):
    for i in range(cnt_personas):
        vector.append([])
        for j in range(3):
            dato = str(input("Digite el " + vector[0][j] + " de la persona: "))
            vector[i + 1].append(dato)


def crear_csv(ubicacion_csv, lista_datos):
    with open(ubicacion_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(lista_datos)


if __name__ == "__main__":
    ubicacion_csv = ' '
    lista_datos = [['id', 'nombre', 'apellido']]
    print("Llenar la lista")
    tam = int(input("Ingrese el tamaño de la lista: "))
    llenar(lista_datos, tam)
    print("*" * 68)
    ubicacion_csv = str(input("Ingrese la ubicacion del archivo: "))
    crear_csv(ubicacion_csv, lista_datos)
