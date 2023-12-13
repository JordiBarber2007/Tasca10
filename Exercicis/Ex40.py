def contar_digits(numero):
    # Comprova que el número estigui dins del rang especificat
    if 1 <= numero <= 900000:
        # Converteix el número a una cadena i compta els dígits
        quantitat_digits = len(str(numero))
        print(f"El número {numero} té {quantitat_digits} dígits.")
    else:
        print("Si us plau, introdueix un número dins del rang entre 1 i 900000.")


# Demana a l'usuari que introdueixi un número
numero = int(input("Introdueix un número: "))

# Executa la funció per contar els dígits del número
contar_digits(numero)