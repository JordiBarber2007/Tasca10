def calcular_suma_quadrats(numero):
    # Comprova si el número és menor que 100
    if numero < 100:
        # Inicialitza la suma
        suma_quadrats = 0

        # Itera pel rang de números separats per quatre posicions fins arribar a 0
        for i in range(numero, 0, -4):
            # Suma el quadrat del nombre actual
            suma_quadrats += i**2

        # Mostra el resultat
        print(f"La suma dels quadrats és: {suma_quadrats}")
    else:
        print("Si us plau, introdueix un número menor que 100.")

# Demana a l'usuari que introdueixi un número
numero = int(input("Introdueix un número del 0-100: "))

# Executa la funció per calcular la suma dels quadrats
calcular_suma_quadrats(numero)