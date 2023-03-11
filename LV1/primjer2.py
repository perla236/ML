from turtle import delay


print("Unesi neki broj između 0.0 i 1.0")
broj = float(input())
try:
    broj = float(broj)
    
except ValueError:
    print("Nije float")


    

if broj < 0.6:
    print("F")
elif broj >= 0.6 and broj <= 0.69:
    print("D")
elif broj >= 0.7 and broj <= 0.79:
    print("C")
elif broj >= 0.8 and broj <= 0.89:
    print("B")
elif broj >= 0.9 and broj <= 0.99:
    print("A")

else:
    print("Broj nije iz intervala")
    


