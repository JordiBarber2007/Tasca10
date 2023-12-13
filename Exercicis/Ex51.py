def llegir_llista_paraules():
    b = []
    a = "a"
    while a != ".":
        a = input("Introdueixi la següent paraula: ")
        if a != ".":
            b.append(a)
    b.sort()
    return b

def index_paraula(llista, paraula):
    return [i for i, e in enumerate(llista) if paraula == e]

# Principal
a = llegir_llista_paraules()
p = input("Introdueix la paraula a cercar el seu índex: ")
b = index_paraula(a, p)

if not b:
    print("Dins la llista {} no hi ha l'element {}".format(a, p))
else:
    print("Dins la llista {} la paraula {} apareix {} vegades en les següents posicions {}".format(a, p, len(b), b))