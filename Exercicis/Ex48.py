from random import randint

def llista_20_elements():
    l = []
    for _ in range(20):
        l.append(randint(1, 100))
    return l

def hi_ha_duplicats(a):
    seen = set()
    dupes = set(x for x in a if x in seen or seen.add(x))
    if dupes:
        print("La llista {} té elements duplicats {}".format(a, dupes))
    else:
        print("La llista {} no té elements duplicats".format(a))

# Principal
x = llista_20_elements()
hi_ha_duplicats(x)