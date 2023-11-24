#Exercici 12. Calculadora
def menu_principal():
    print("""
      Menú principal:
      1. Calculadora de nombre enters
      2. Calculadora de nombre reals
      3. Canvis de base
      4. Sortir
          
      """)
    a = int(input("Elegeixi una opció: "))
    return a
def calculadora_enters():
    op = 1
    while op>0:
        print("""
            Menú enters:
                1. Sumar
                2. Resta
                3. Multiplicar 
                4. Dividir
                5. Sortir
              """)
        
        op = int(input("Elegeix una opció: "))
        match op:
            case 1: #Sumar
                a = int(input("Introdueix un nombre: "))
                b = int(input("Introdueix el segon nombre per sumar: "))
                print("La suma de {} + {} = {}".format(a,b, a+b))

            case 2: #Restar
                a = int(input("Introdueix un nombre: "))
                b = int(input("Introdueix el segon nombre per restar: "))
                print("La resta de {} - {} = {}".format(a,b, a-b))

            case 3: #Multiplicar
                a = int(input("Introdueix un nombre: "))
                b = int(input("Introdueix el segon nombre per multiplicar: "))
                print("La multiplicació de {} * {} = {}".format(a,b, a*b))

            case 4: # Dividir
                a = int(input("Introdueix un nombre: "))
                b = int(input("Introdueix el segon nombre per dividir: "))
                print("La divició de {} / {} = {}".format(a,b, a/b))
                
            case 5: # Sortir
                op = -1

def calculadora_reals():
    op = 1
    while op>0:
        print("""
            Menú enters:
                  1. Sumar
                  2. Resta
                  3. Multiplicar
                  4. Dividir
                  5. Sortir
                 """)
        op = int(input("Elegeix una opció: "))
        match op:
            case 1: # Sumar
                a = float(input("Introdueixi el primer número: "))
                b = float(input("Introdueixi el segon número: "))
                print("{} + {} = {}".format(a, b, a+b))

            case 2: # Restar
                a = float(input("Introdueixi el primer número: "))
                b = float(input("Introdueixi el segon número: "))
                print(" {} - {} = {}".format(a, b, a-b))

            case 3: # Multiplicar
                a = float(input("Introdueixi el primer  número: "))
                b = float(input("Introdueix el segon número: "))
                print("{} * {} = {}".format(a, b, a*b))

            case 4: # Dividir
                a = float(input("Introdueixi el primer número: "))
                b = float(input("Introdueix el segon número "))
                print("La divició de {} / {} = {}".format(a, b, a/b))
            case 5: # Sortir
             print(" Adéu, ja tornaràs a la calculadora inicial \n\n*")
             op=-1
             
# Funcions de canvis de base
# De decimal a binari, octal i hexadecimal
def dectobin(numero):
    # Prec: numero sigui un enter
    # Post: Escriu el valor de l'enter en binari
   return bin(numero)
def dectooct(numero):
    # Prec: numero sigui un enter
    # Post: Escriu el valor de l'enter en octal
   return oct(numero)
def dectohex(numero):
    # Prec: numero sigui un enter
    # Post: Escriu el valor de l'enter en hexadecimal
   return hex(numero)
# De binari a octal, decimal, hexadecimal
def bintooct(numero):
    # Prec: numero sigui una cadena de caracters
    # Post: escriu el número en octal
    a=int(numero,2)
    return dectooct(a)
def bintodec(numero):
    # Prec: numero sigui una cadena de caracters i en binari
    # Post: escriu el número en decimal
    a=int(numero,2)
    return a
def bintohex(numero):
    # Prec: numero sigui una cadena de caracters i en binari
    # Post: escriu el número en hexadecimal
    a=int(numero,2)
    return dectohex(a)   
# Octal a binari, decimal i hexadecimal
def octtobin(numero):
    # Prec: numero sigui una cadena de caracters i en octal
    # Post: escriu el número en hexadecimal
    a=int(numero,8)
    return dectobin(a)
def octtodec(numero):
    # Prec: numero sigui una cadena de caracters i en octal
    # Post: escriu el número en decimal o millor dit, el retorna
    a=int(numero,8)
    return a
def octtohex(numero):
    # Prec: numero sigui una cadena de caracters i en octal
    # Post: escriu el número en hexadecimal o millor dit, el retorna
    a=int(numero,8)
    return dectohex(a)   

# Hexadecimal a binari, octal i decimal
def hextonum(hex): # Aquesta funció passa quasevol hexadecimal a un numero
    pnum = {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10
     }
    if hex in pnum:
        return pnum[hex]
    else:
        return int(hex)
def hextodec2(hex):
    hex = hex.lower()
    hex = hex[ : : -1]
    decimal = 0
    posicio = 0
    for digit in hex:
        valor = hextonum(digit)
        elevat = 16 ** posicio
        pnum = elevat * valor
        decimal += pnum
        posicio +=1
    return decimal
def hextobin(numero):
    a=int(numero,16)
    return dectobin(a)
def hextooct(numero):
    a=int(numero,16)
    return dectooct(a)
def hextodec(numero):
    a = int(hextodec2(numero))
    return a
def canvi_base():
    op = 1
    while op>0:
        print("""
            Menu canvis de base:
                 1. Donat un binari ho passem a tota la resta
                 2. Donat a un octal el passam a tota la resta
                 3. Donat un decimal ho passem a tota la resta
                 4. Donat un hexadecimal ho passem a tota la resta
                 5. Sortir
                 """)
        op = int(input("Elegeixi una opció: "))
        match op:
            case 1: # Binari to
              b = input("Introdueixi el número binari: ")
              o = bintooct(b)
              d = bintodec(b)
              h = bintohex(b)
              print("El número binari {} és: \n oct -> {} \n hex -> {}".format(b,o,d,h))
            case 2: # Octal to
              o = input("Introdueixi el número octal: ")
              b = octtobin(o)
              d = octtodec(o)
              h = octtohex(o)
              print("El número octal {} és: \n bin -> {} \n hex -> {}".format(b,o,d,h))
            case 3: # Decimal to
              d = input("Introdueixi el número decimal: ")
              b = dectobin(d)
              o = dectooct(d)
              h = dectohex(d)
              print("El número decimal {} és: \n bin -> {} \n hex -> {}".format(b,o,d,h))
            case 4: #Hexadecimal to
              h = input("Introdueixi el número Hexadecimal: ")
              b = hextobin(h)
              o = hextooct(h)
              d = hextodec(h)
              print("El número hexadecimal {} és: \n bin -> {} \n hex -> {}".format(b,o,d,h))
            case 5: #Sortir
              print("Adéu, tornaràs a la calculadora inicial \n\n")
              op=-1 

    
#Programa principal
a = 1
while a>0:
    a = menu_principal() 
    match a:
        case 1:
            calculadora_enters()
        case 2:
            calculadora_reals()
        case 3:
            canvi_base()
        case 4:
            print("Adeu")
            opcio = -1