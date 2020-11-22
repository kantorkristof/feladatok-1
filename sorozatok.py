#1 feladat
lista = open("lista.txt")
listaadat = lista.read()
print(listaadat)
#2 feladat

#3 feladat
print("3. feladat")
listarange = len(listaadat) 
print (listarange)
latott=0
nemlatott=0
for i in range(listarange):
    if i=="0":
        nemlatott=nemlatott+1
    elif i=="1":
        latott=latott+1
print(latott)
print(nemlatott)

