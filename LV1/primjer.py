def total_euro(a, b):
    return a*b

print("Upišite broj radnih sati radnika:\n")
placa = int(input())
print("Koliko je placen po satu:\n")
satRada = int(input())
#total_euro = placa*satPara  //to kad neamo funkciju....
print("Radnik je zaradio ", total_euro(placa,satRada),  "eura")
