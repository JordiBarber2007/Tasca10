def imprimir_taula_multiplicar(numero):
    # Comprova que el número estigui dins del rang especificat
    if 1 <= numero <= 20:
        print(f"Taula de multiplicar del {numero}:")
        # Bucle per imprimir la taula de multiplicar
        for i in range(1, 11):
            resultat = numero * i
            print(f"{numero} x {i} = {resultat}")
    else:
        print("Si us plau, introdueix un número dins del rang entre 1 i 20.")


# Demana a l'usuari que introdueixi un número
numero = int(input("Introdueix un número: "))

# Executa la funció per imprimir la taula de multiplicar del número donat
imprimir_taula_multiplicar(numero)