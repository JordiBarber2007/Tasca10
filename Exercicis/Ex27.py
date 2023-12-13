def mayusculas(lista):
    result = []
    for palabra in lista:
        if any(char.isupper() for char in palabra):
            result.append(palabra)
    return result

lista = input("Ingrese una lista de palabras separadas por comas: ").split(',')

resultado = mayusculas(lista)

print("Las palabras que contienen una mayúscula son:", resultado)