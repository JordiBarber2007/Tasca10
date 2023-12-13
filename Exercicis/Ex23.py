def crear_punts(llista):
    for num in llista:
        print("." * num)

def dibuixar_imatge(imatge):
    for linia in imatge:
        crear_punts(linia)

# Ejemplo de uso
imatge_a_dibuixar = [
    [7, 3, 4, 3, 7],
    [5, 6, 5],
    [7, 6, 8, 2, 5],
    [4, 3, 1, 2, 6, 3, 7]
]

dibuixar_imatge(imatge_a_dibuixar)