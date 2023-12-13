# Defineix el nombre de vegades que vols imprimir la sèrie
vegades = 5

# Bucle extern per imprimir la sèrie 5 vegades
for _ in range(vegades):
    # Bucle intern per imprimir la sèrie de l'1 al 15
    for numero in range(1, 16):
        print(numero, end=' ')

    # Salta una línia entre cada sèrie
    print()