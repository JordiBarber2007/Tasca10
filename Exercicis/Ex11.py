def menu_principal():
    a = 1
    while a>0:
        print("""
            menu_principal:
                1. Calculadora enteros
                2. Calculadora reales
                3. Canvis de base
                4. salida
            """)
        a = int(input("Elige la opción: "))
        if a>0 and a<5:
            return a
        else:
            print("Vuelve a Intentarlo: \n")

def calculadora_enters():
    print("Calculadra de enters")
    op = 1
    while op>0:
        print(""""
            Calculadora de enters
                1. Sumar
                2. Resta
                3. Multiplicación
                4. División
                5. Sortir
              """)
        op = int(input("Elige la opción: "))
        match op:
            case 1: #Sumar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introdueix el segon nombre: "))
                print("{} + {} = {}".format(x, y, x+y))
            case 2: #Restar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introdueix el segon nombre: "))
                print("{} - {} = {}".format(x, y, x-y))
            case 3: #Multiplicar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introdueix el segon nombre: "))
                print("{} * {} = {}".format(x, y, x*y))
            case 4: #Dividir
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introdueix el segon nombre: "))
                print("{} / {} = {}".format(x, y, x/y))
            case 5: #Sortir
                print("Adeu, ja tornaras a la calculadora inicial \n\n")
                op=-1

def calculadora_reals():
    print("Calculadora de reals")
    op2 = 1
    while op2>0:
        print(""""
            Calculadora de enters
                1. Sumar
                2. Resta
                3. Multiplicación
                4. División
                5. Sortir
              """)
        op2 = int(input("Elige la opción: "))
        match op2:
            case 1: #Sumar
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introdueix el segon nombre: "))
                print("{} + {} = {}".format(x, y, x+y))
            case 2: #Restar
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introdueix el segon nombre: "))
                print("{} - {} = {}".format(x, y, x-y))
            case 3: #Multiplicar
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introdueix el segon nombre: "))
                print("{} * {} = {}".format(x, y, x*y))
            case 4: #Dividir
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introdueix el segon nombre: "))
                print("{} / {} = {}".format(x, y, x/y))
            case 5: #Sortir
                print("Adeu, ja tornaras a la calculadora inicial \n\n")
                op2=-1

def canvi_de_base():
    print("Canvi de base")
    op3 = 1
    while op3>0:
        print(""""
            Canvi de base
                1. Binari
                2. Octal
                3. Hexadecimal
                4. Sortir
              """)
        op3 = int(input("Elige la opción: "))
        match op3:
            case 1: #Binari
                x = int(input("Introdueix un nombre: "))
                print(bin(x))
            case 2: #Octal
                x = int(input("Introdueix un nombre: "))
                print(oct(x))
            case 3: #Hexadecimal
                x = int(input("Introdueix un nombre: "))
                print(hex(x))
            case 4: #Sortir
                print("Adeu, ja tornaras a la calculadora inicial \n\n")
                op3=-1

#Programa principal
opcio = 1
while opcio>0:
        opcio =  menu_principal()
        match opcio:
            case 1:
                calculadora_enters()
            case 2:
                calculadora_reals()
            case 3:
                canvi_de_base()
            case 4:
                print("Sortir")
                opcio=-1