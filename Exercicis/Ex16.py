def es_vocal(c):
    return c.lower() in ['a', 'e', 'i', 'o', 'u']

# Ús de la funció
lletra = input('Introdueixi una lletra per a veure si és vocal o no: ')
if es_vocal(lletra):
    print('És vocal!')
else:
    print('No és vocal!')