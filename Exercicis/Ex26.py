def filtrar_paraules(llista_paraules, x):
    for paraula in llista_paraules:
        if len(paraula) > x:
            print(paraula)

a = input("Introdueix una llistan de paraules separades per espais: ")

paraules = a.split()

x = int(input("Introdueix el mínim de caràcters que tenen que tenir: "))

print("Paraules amb més de {} caràcters:".format(x))

filtrar_paraules(paraules, x)