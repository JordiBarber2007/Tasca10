a = 1
while a>0:
    print("""
    Menú
    1. Mirar si un número és senar o parell
    2. Sortir
    """)
    a = int (input("Seleccioni una opció: "))
    match a:
        case 1: #Si volem veure si un número és o no parell
            x = int(input("Introdueixi un nombre:"))
            if x % 2 == 0:
                print("És parell")
            else:
                print("És senar (impar)")
        case 2:
            a =0