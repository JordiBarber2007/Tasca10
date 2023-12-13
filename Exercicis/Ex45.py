def llegir_llista():
    a = []
    c = "a"
    while c != ".":
        c = input("Introdueixi un element de la llista i punt (.) per acabar: ")
        if c != ".":
            a.append(c)
    return a

def eliminar_capicua(a):
    b = []
    if len(a) > 2:
        b = a[1:-1]
    return b

# Principal
x = llegir_llista()
y = eliminar_capicua(x)
print("La llista original {} s'ha transformat en la llista {}".format(x, y))