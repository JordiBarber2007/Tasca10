def es_palindrom(paraula):
    #Convertim tots els carácters en minúscules per considerar la majúscula y minúscula equivalents.
    paraula = paraula.lower()
    return paraula == paraula[::-1]

#Exemples d'ús
print(es_palindrom("moto"))   
print(es_palindrom("arbr"))     
print(es_palindrom("civic"))  
print(es_palindrom("ca"))  
print(es_palindrom("tapat"))   
print(es_palindrom("casa"))   
print(es_palindrom("refer")) 