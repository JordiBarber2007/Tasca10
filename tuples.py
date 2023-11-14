def tercera_ocurrencia(l,e):
    a = l.count(e)
    if a==0:
        print("No hi ha ocurrencies d'aquest element")
    elif a==1:
        print("La primera ocurrencia de l'element està en la posició {}".format(l.index(e)))
    elif a==2:
        print("Hi ha més d'una ocurrencia de {}".format(e))
        p = l.index(e)
        so = l.index(e,(p+1))
        print(so)
    elif a>2:
        print("Hi ha més d'una ocurrencia de {}".format(e))
        p = l.index(e)
        so = l.index(e,(p+1))
        to = l.index (e, (so+1))
        print(to)
    else:
        print("Valor no valid")
#Programa princuipal
l=(1, 4, 2, (1, 3, 3), 3, 4, 2, 1, 4, 2, 1)
x = int(input("Elegeixi l'element que vol cercar la 3a ocurrencia: "))
tercera_ocurrencia(l,x)