def elements_parells(a):
    for i, e in enumerate(a):
        if i % 2 == 1:
            print(e)

def llegir_llista():
    l = []
    a = 'a'
    while a != '.':
        a = input("Introduexi una nova paraula i punt (.) per acabar:")
        if a != '.':
            l.append(a)
    return l

# Principal
b = llegir_llista()
elements_parells(b)