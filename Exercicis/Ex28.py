def bintodec(num):
    return int(num,2)

num = input("Introdueix un número en binari: ")
a = bintodec(num)
print("Numero binari {}  passat a enter {}".format(num,a))