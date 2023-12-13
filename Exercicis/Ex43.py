suma=0
a = input("Introdueix un número: ")
print("{} té {} dígits".format(a,len(a)))
for i in a:
	suma = suma + int(i)
print("La suma dels dígits del número {} és {}".format(a,suma))
if suma%2==0:
	print("La suma dels dígits del número {} és parell".format(a))
else:
	print("La suma dels dígits del número {} és senar".format(a))