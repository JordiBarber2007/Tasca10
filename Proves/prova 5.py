def llegir_llista():
    a = '1'
    l=[]
    while a!='a':
        a=input("Introdueixi un número diferent a 'a': ")
        if a !='a':
            l.append(int(a))
        else:
            return l
        
#Programa principal
a = llegir_llista()
b = llegir_llista()
c=[]
for i in range(len(a)):
    c.appende(a[i]*b[i])
print("La multiplicació de la llista {} per la llista {} és {}".format(a,b,c,))