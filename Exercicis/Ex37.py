def comprova_rima(paraula1, paraula2):
    # Obtenim les últimes 3 lletres de cada paraula
    ultimes_3_lletres_paraula1 = paraula1[-3:]
    ultimes_3_lletres_paraula2 = paraula2[-3:]

    # Obtenim les últimes 2 lletres de cada paraula
    ultimes_2_lletres_paraula1 = paraula1[-2:]
    ultimes_2_lletres_paraula2 = paraula2[-2:]

    # Comprovem si rimen totalment o una mica
    if ultimes_3_lletres_paraula1 == ultimes_3_lletres_paraula2:
        return "Les paraules riman totalment."
    elif ultimes_2_lletres_paraula1 == ultimes_2_lletres_paraula2:
        return "Les paraules riman un poc."
    else:
        return "Les paraules no riman."

# Demanem a l'usuari les dues paraules
paraula1 = input("Introdueix la primera paraula: ")
paraula2 = input("Introdueix la segona paraula: ")

# Truquem a la funció i mostrem el resultat
resultat = comprova_rima(paraula1, paraula2)
print(resultat)