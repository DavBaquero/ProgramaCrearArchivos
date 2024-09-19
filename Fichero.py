def main():
    nombre = input("Ponle nombre al archivo: ")
    conta = 0
    while len(nombre) < 1:
        if conta < 2:
            nombre = input("Ponle nombre al archivo: ")
            conta += 1
        else:
            exit("No has escrito nada")

    nombre = nombre + ".txt"
    with open(nombre, "w") as n:
        n.write(input("Que quieres escribir en el archivo: "))

    with (open(nombre, "r") as leer):
        contenido = leer.read()
        vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú", "ü"]
        posicion = 0
        total = 0
        for vocal in vocales:
            vocales[posicion] = vocal
            contmin = contenido.lower()
            sumatorio = contmin.count(vocal)
            total = total + sumatorio
            posicion = posicion + 1
        print("El archivo contiene:", contenido)
        print("El archivo tiene: ", total, "vocales.")

    with open(nombre, "a") as f:
        f.write('\n' + input("Que quieres escribir en el archivo: "))

    with (open(nombre, "r")) as leer:
        contenido = leer.read()
        print("El archivo contiene:", contenido)

    respuesta = (input("¿Quieres escribir más? Si es sí, escribe 'y', si es no 'n': "))
    while respuesta == "y":
        with open(nombre, "a") as f:
            f.write('\n' + input("Que quieres escribir en el archivo: "))

        with (open(nombre, "r")) as leer:
            contenido = leer.read()
            print("El archivo contiene:", contenido)

        if respuesta == "y":
            respuesta = (input("¿Quieres seguir? Si es sí, escribe 'y', si es no 'n': "))

main()