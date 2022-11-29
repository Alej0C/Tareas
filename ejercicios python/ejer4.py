import os


def llenar(vector):
    for i in range(3):
        dato = str(input("Digite el usuario: "))
        vector.append(dato)


def crear_usuario(vector):
    for i in range(len(vector)):
        dato = str(vector[i])
        command_line = 'adduser ' + dato
        linea = str(command_line)
        os.system(linea)
        print("El usuario fue creado", dato)


if __name__ == "__main__":
    lista_datos = []
    print("Llenar la lista")
    llenar(lista_datos)
    print(lista_datos)
    print("*" * 42)
    crear_usuario(lista_datos)
