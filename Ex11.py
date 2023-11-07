#Exercici 11. Calculadora
def  menu_principal():
    print("""
        Menú principal:
        1. Calculadora de números enters
        2. Calculadora de numeros reals
        3. Sortir
        
    """)
    a = int(input("Elegeix una opció: "))
    return a
def calculadora():
    op = 1
    while op>0:
        print("""
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Sortir
        """)
        op = int(input("Elegeixi una opció: "))
        match op:
            case 1: # Sumar
                x = int(imput("Introdueixi el primer número: "))
                y = int(imput("Introdueixi el segon número: "))
                print("{} +  {} = {}".format(x, y, x+y))
            case 2: #Restar
                x = int(imput("Introdueixi el primer número: "))
                y = int(imput("Introdueixi el segon número: "))
                print("{} +  {} = {}".format(x, y, x+y))
            case 3: # Multiplicar
                x = int(imput("Introdueixi el primer número: "))
                y = int(imput("Introdueixi el segon número: "))
                print("{} +  {} = {}".format(x, y, x+y))
            case 4: # Dividir
                x = int(imput("Introdueixi el primer número: "))
                y = int(imput("Introdueixi el segon número: "))
                print("{} +  {} = {}".format(x, y, x+y))
            case 5: # Sortir
                