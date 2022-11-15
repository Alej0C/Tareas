def llenar(vector, t):
    for i in range(t):
        print("Ingrese el dato en la posición: " + "" + str(i) + " ")
        dato = int(input())
        vector.append(
            dato
        )  #para llenar un vector en cada posición se utiliza la función append debido a que esta inicia a llenar el vector desde la posición 0 hasta que se cumpla la condición del ciclo


def imprimir(vector, t):
    for i in range(t):
        print("Vector [" + "" + str(i) + "]= " + "" + str(vector[i]))


def ordenar_mayor_menor(vector, t):
    for i in range(t):
        for j in range(t):
            if vector[i] > vector[j]:
                aux = vector[i]
                vector[i] = vector[j]
                vector[j] = aux


def ordenar_menor_mayor(vector, t):
    for i in range(t):
        for j in range(t):
            if vector[i] < vector[j]:
                aux = vector[i]
                vector[i] = vector[j]
                vector[j] = aux


def sumadatos(vector, t):
    s = 0
    for i in range(t):
        s += vector[i]
    print("La suma de los datos del vector es: " + "" + str(s) + " ")


def buscar(vector, t, nb):
    indice = -1
    for i in range(t):
        if vector[i] == nb:
            indice = i
    if indice == -1:
        print("Dato No encontrado")
    else:
        print(str(nb) + " se encuentra en la posición: " + "" + str(indice))


def eliminar(vector, ne):
    i = 0
    while i < len(vector):
        if vector[i] == ne:
            vector.pop(
                i
            )  #La función pop funciona en la eliminación de la posición del vector, este elimina la posición del vector
            print(
                str(ne) +
                " ha sido eliminado, se encontraba en la posición: " + "" +
                str(i))
        else:
            i += 1


t = int(input("Ingrese el tamaño del vector "))
vector = []
print("llenar Vector")
llenar(vector, t)
print("Imprimir Vector")
imprimir(vector, t)
print("ordenar vector")
ordenar_mayor_menor(vector, t)
print("Imprimir Vector ordenado de mayor a menor")
imprimir(vector, t)
ordenar_menor_mayor(vector, t)
print("Imprimir Vector ordenado de menor a mayor")
imprimir(vector, t)
print("Buscar un número dentro del vector")
nb = int(input("Ingrese el número a buscar: "))
buscar(vector, t, nb)
print("Suma de los datos del vector")
sumadatos(vector, t)
ne = int(input("Ingrese el número a eliminar: "))
eliminar(vector, ne)
t = len(vector)
imprimir(vector, t)
