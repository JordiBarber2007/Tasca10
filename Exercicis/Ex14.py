#Definir una funció gran_de_tres(), donats tres números, retorni el major. Prova-la amb diferents exemples.
def numero_mayor():
    a = int(input("Introdueix un número: "))
    b = int(input("Introdueix un número: "))
    c = int(input("Introdueix un ultimo número: "))
    if a>b>c:
        print("El número major entre {} , {} i {} és {}".format(a, b, c, a))
    elif a>c>b:
        print("El número major entre {} , {} i {} és {}".format(a, b, c))
    elif b>a>c:
        print("El número major entre {} , {} i {} és {}".format(b, a, c, b))
    elif b>c>a:
        print("El número major entre {} , {} i {} és {}".format(b, c, a, b))
    elif c>a>b:
        print("El número major entre {} , {} i {} és {}".format(c, a, b, c))
    elif c>b>a:
        print("El número major entre {} , {} i {} és {}".format(c, b, a, c))
    elif b>c and a==c:
        print("El número major entre {} , {} i {} és {} i {} i {} son iguals".format(a, b, c, b, c, a))
    elif c>a and a==b:
        print("El número major entre {} , {} i {} és {} i {} i {} son iguals".format(a, b, c, c, a, b))
    elif a>b and b==c:
        print("El número major entre {} , {} i {} és {} i {} i {} son iguals".format(a, b, c, a, b, c))
    elif a==b and a>c:
        print("El número major entre {} , {} i {} és {} i {} i el menor es {} ".format(a, b, c, a, b, c))
    elif c==a and a>b:
        print("El número major entre {} , {} i {} és {} i {} i el menor es {} ".format(a, b, c, a, c, b))
    elif c==b and c>a:
        print("El número major entre {} , {} i {} és {} i {} i el menor es {} ".format(a, b, c, b, c, a))
    else:
        print("Todos los numeros són iguals".format(a, b, c))

def menu():
    print("1. Comparar números")
    print("2. Salir")
    return int(input("Introduce una opción: "))

#Programa principal
opcio = 1
while opcio>0:
    opcio = menu()
    match opcio:
        case 1:
            numero_mayor()
        case 2:
            opcio=-1
        case other:
            print("Opció no vàlida")