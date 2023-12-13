def superposició(llista1, llista2):
    return bool(set(llista1) & set(llista2))
#Llista x i z
llista_x = [6, 7, 8, 9]
llista_z = [777, 69, 6, 50]

resposta = superposició(llista_x, llista_z)

print(resposta)