def canvi(l,m,n):
    print("1) {}{} \n {}".format(l, m,n))
    l='Adeu, '
    m='Joan'
    n='Que vagi bé'
    print("2) {}{} \n {}".format(l, m,n))
    return l,m,n
#Programa principal
a="Hola,"
b="Ramis,"
c="Com estàs?"
print("El valor de la variable abans de canviar és: {}{}\n {}".format(a, b, c))
canvi(a, b, c)
print("El valor de la variable després de canviar és: {}{} \n {}".format(a, b, c))


("""def intercanvi(a,b):
    return b,a 
x='a'
y='b'
print("El valor d'x és {} i el d'y és {}".format(x,y))
x,y = intercanvi(x,y)
print("Després de l'intercanvi, el valor d'x és {} i el d'y és {}".format(x,y))


a = int(input("Introdueixi un 1r nombre: "))
b = int(input("Introdueixi un 2n nombre: "))
c = major(a,b)
print("El major de {} i {} és {}".format(a, b, c))




def canvi(l):
#Codi que te diu quina posició vols modificar i quin valor vols inse rir.
    x= input("Introdueix la posició a modificar: ")
    l[x]=input("Introdueix el valor a inserir: ")
#Programa principal
#Llista, cadena de caracters, tuples que haura de modificar.
a=[3, 4, 5, 6, 7, 8, 'a', (1,2),[3,4],10]
print("El valor de la llista abans de canviar és: {}".format(a))
canvi(a)
print("El valor de la llista després de canviar és: {}".format(a))



def canvi(l):
    l=(1,2,6, 8)
#Programa principal
a=(3, 5, 7, 9, 10)
print("El valor de la tupla abans de canviar és: {}".format(a))
canvi(a)
print("El valor de la tupla després de canviar és: {}".format(a))




 def canvi(l):
    x=int(input("Introdueix el valor a inserir: "))
    l.add(x)
#Programa principal
a={'a':3, 5, 7, 9, 10}
print("El valor del conjunt abans de canviar és: {}".format(a))
canvi(a)
print("El valor del conjunt després de canviar és: {}".format(a))


""")