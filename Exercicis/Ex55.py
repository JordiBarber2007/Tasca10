def dibuixar(a):
    l = []
    for j in range(a + 1):
        for i in range(j):
            l.append('*')
        print(' '.join(map(str, l)))
        l.clear()

    for j in range(a + 1, 0, -1):
        for i in range(j):
            l.append('*')
        print(' '.join(map(str, l)))
        l.clear()

# Principal
a = int(input("Introdueixi un número: "))
dibuixar(a)