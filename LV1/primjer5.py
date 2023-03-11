with open('song.txt', 'r') as datoteka:
    rijeci = datoteka.read().split()

brojRijeci = {}

for rijec in rijeci:
    if rijec not in brojRijeci:
        brojRijeci[rijec] = 1
    else:
        brojRijeci[rijec] += 1

jednaRijec = []

for rijec, brojac in brojRijeci.items():
    if brojac == 1:
        jednaRijec.append(rijec)

print(f"Broj riječi koje se pojavljuju samo jednom: {len(jednaRijec)}")
print("Riječi koje se pojavljuju samo jednom:")
for rijec in jednaRijec:
    print(rijec)

    datoteka.close()
