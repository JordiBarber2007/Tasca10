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
    llista=[]
    print("Introdueixi noms a la llista, per acabar posau -1: ")

    while i>-1:
        llista.append(input("Posi el següent nom: "))
        if (llista[i]=="-1"):
            llista.remove("-1")
            i=-5
            i+=1
            return llista
    
# Programa principal
noms = llegir_noms()
caracter = input("Introdueixi el caràcter que vols que comencin les paraules a cercar: ")
noms_que_comencen_per(noms,caracter)