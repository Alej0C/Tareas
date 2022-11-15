def llenar(vector, t):
    for i in range(t):
        print(f"Ingrese el dato en la posición: " + "" + str(i) + " ")
        dato = str(input())
        vector.append(dato)


def imprimir(vector, t):
    for i in range(t):
        print("Lista [" + "" + str(i) + "]= " + "" + str(vector[i]))


def buscar(vector, t, nb):
    indice = -1
    for i in range(t):
        if vector[i] == nb:
            indice = i
    if indice == -1:
        print("Dato No encontrado")
    else:
        print(str(nb) + " se encuentra en la posición: " + "" + str(indice))


def reemplazar(vector):
    aux1 = vector[0]
    tam = len(vector) - 1
    aux2 = vector[tam]
    vector[0] = aux2
    vector[tam] = aux1


if __name__ == "__main__":
    t = int(input("Ingrese el tamaño de la lista: "))
    vector = []
    print("llenar lista")
    llenar(vector, t)
    print("Imprimir lista")
    imprimir(vector, t)
    print("Buscar una palabra dentro de la lista")
    nb = str(input("Ingrese la palabra a buscar: "))
    buscar(vector, t, nb)
    print("\n")
    reemplazar(vector)
    print(vector)
