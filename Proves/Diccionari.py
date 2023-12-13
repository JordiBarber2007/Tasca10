dic = {'nom':'Joan','cognom':'Ramis','edat':30,'telèfon':'971360133'}
for element in dic:
    print("La clau {} té el valor {}".format(element,dic[element]))
# Segona forma
for x,y in dic.items():
    print("La clau és {} i el seu valor és {}".format(x,y))
#dic.clear()
b={'nom':'Pere', 'carrer':'Vives Llull, 15', 'Plantes':2}
dic.update(b)
print(dic)