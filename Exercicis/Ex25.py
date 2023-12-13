def llegir_llista():
    # Anirà llegint elements d'una llista (Aquí enters)
    # Retornarà la llista creada
    a=' '
    l=[]
    while a!='.':
        a = input("Introdueix un nou element de la llista: ")
        if a!=".":
            l.append(a) # Introdueix paraules
        else:
            return l

def paraula_mes_llarga(llista_paraules):
    if not llista_paraules:
        return None 

    paraula_mes_llarga = llista_paraules[0]

    for paraula in llista_paraules:
        if len(paraula) > len(paraula_mes_llarga):
            paraula_mes_llarga = paraula

    return paraula_mes_llarga

resultat = paraula_mes_llarga(llegir_llista)
print(resultat)