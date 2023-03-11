import math
print("unosite koliko god hocete brojeva i kad ste gotovi upišite ""Done"":")
lista=[]
brojevi = 0
brojac = 0
suma = 0
srednja = 0
while brojevi != "Done":
    
    brojevi = input()
    #brojevi = float(brojevi)
    if brojevi.isdigit():
        brojevi = float(brojevi)
        lista.append(brojevi)
    brojac= brojac + 1
    if brojevi == "Done":
        #lista.pop(-1)
        
        lista.sort()
        suma = sum(lista)
        #srednja = suma / brojac 
        print("Srednja vrijednost je: ",suma, "\n")
        print("Najveci element je " ,max(lista), "\n")
        print("Najmanji element je " ,min(lista), "\n")
        print(*lista)

        break
