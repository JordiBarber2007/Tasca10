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