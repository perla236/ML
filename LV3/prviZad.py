import pandas as pd
import numpy as np

mtcars = pd.read_csv('mtcars.csv')
print("Kojih 5 automobila ima najveću potrošnju?")
print(mtcars.sort_values(by=['mpg'], ascending = False).head(5))

print("\n")

print("Koja tri automobila s 8 cilindara imaju najmanju potrošnju?")

osamCilindara = mtcars[mtcars["cyl"] == 8]
najmanjaPotrosnjaOsam = osamCilindara.sort_values(by=['mpg']).head(3)
print(najmanjaPotrosnjaOsam[["car", "mpg"]])


print("\n")


print("Kolika je srednja potrošnja automobila sa 6 cilindara?")
sestCilindara = mtcars[mtcars["cyl"] == 6]
print(sestCilindara["mpg"].mean())


print("\n")


print("Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?")
#cetriCilindra = mtcars[mtcars["cyl"] == 4 & mtcars["wt"] > 2 & mtcars["wt"] < 2.2]
cetriCilindra = mtcars[(mtcars.cyl == 4) & (mtcars.wt >= 2) & (mtcars.wt <= 2.2)]
print(cetriCilindra["mpg"].mean())


print("\n")


print("Koliko je automobila s ručnim, a koliko s automatskim mjenjačem u ovom skupu podataka?")
brojAutomatskihMjenjaca = mtcars[mtcars["am"] == 0]
brojRucnihMjenjaca = mtcars[mtcars["am"] == 1]

print("Automatskih je {}".format(brojAutomatskihMjenjaca.shape[0]))
print("Rucnih je {}".format(brojRucnihMjenjaca.shape[0]))


print("\n")


print("Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?")
automatskiSnaga = mtcars[(mtcars.am == 0) & (mtcars.hp > 100)]
print("Broj auta je {}".format(automatskiSnaga.shape[0]))

print("\n")

print("Kolika je masa svakog automobila u kilogramima?")
masaKilogrami = mtcars.wt * 1000 * 0.45359237
print(masaKilogrami)








