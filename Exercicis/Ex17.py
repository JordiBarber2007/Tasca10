#Suma de la llista 
def sumar_llista(llista):
    suma = 0
    for valor in llista:
        suma += valor
    return suma 
exemple_llista = sumar_llista([2, 30, 4, 50])
print(f"Sumar: {exemple_llista}")

# Multiplicació llista
def multiplicar_llista(llista):
    producte = 1
    for valor in llista:
        producte *= valor 
    return producte 
exemple_llista = multiplicar_llista([2, 30, 4, 50])
print(f"Multiplicació: {exemple_llista}")