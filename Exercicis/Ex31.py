def noms_que_comencen_per(llista,lletra):
    comptador = 0
    llnom= []
    for e in llista:
        if e[0]==lletra:
            llnom.append(e)
            comptador += 1
            print("El número de noms que comencen per el caràcter {} són: {} i són: {}".format(lletra, comptador, llnom))

def llegir_noms():
    i=0
    l=[]
    print("Introdueixi noms a la llista, per acabar posau -1: ")
    while i>-1:
        l.append(input("Posi el següent nom: "))
    if (l[i]=="-1"):
        l.remove("-1")
        i=-5
        i+=1
        return l
        
# Programa principal
noms = llegir_noms()
noms_que_comencen_per(noms,"a")