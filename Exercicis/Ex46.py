def esta_ordenada(a):
    b = a.copy()
    a.sort()
    if a == b:
        print("La llista {} està ordenada {}".format(a, b))
    else:
        print("La llista {} no està ordenada {}".format(a, b))

def llegir_llista():
    a = []
    c = "a"
    while c != ".":
        c = input("Introdueixi un element de la llista i punt (.) per acabar: ")
        if c != ".":
            a.append(c)
    return a

# Principal
a = llegir_llista()