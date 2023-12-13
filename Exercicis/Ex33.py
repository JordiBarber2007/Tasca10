def comptar_vocals(a):
    b = ('a','e','i','o','u','altres')
    vocals=[0,0,0,0,0,0]
    for i,e in enumerate(a):
        if e=='a' or e=='A' or e=='à' or e=='á' or e=='À' or e=='Á':
            vocals[0]+=1
        elif e=='e' or e=='E'or e=='è' or e=='é' or e=='È' or e=='É':
            vocals[1]+=1
        elif e=='i' or e=='I'or e=='í' or e=='Í' :
            vocals[2]+=1
        elif e=='o' or e=='O'or e=='ò' or e=='ó' or e=='Ò' or e=='Ó':
            vocals[3]+=1
        elif e=='u' or e=='U'or e=='ú' or e=='Ú':
            vocals[4]+=1
        else:
            vocals[5]+=1
        for i,e in enumerate(vocals):print("La vocal {} apareix {} vegades".format(b[i], vocals[i]))

#PPrincipal
a = input("Introdueixi una paraula a analitzar: ")
comptar_vocals(a)