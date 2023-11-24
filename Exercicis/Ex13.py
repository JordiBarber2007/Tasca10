def gran(x,y):
    if x > y:
        return x
    elif y > x:
        return y
#Programa principal
x=int(input("Introdueix el primer valor: "))
y=int(input("Introdueix el segon valor: "))
z=gran(x,y)
print("El valor major és {} :".format(z))