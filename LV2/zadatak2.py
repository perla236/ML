import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),
delimiter=",", skiprows=1)

mpg = data[:, 0]
hp = data[:, 3]
wt = data[:, 5]

plt.scatter(hp,mpg,s= wt*100,)
plt.xlabel('Konjske snage')
plt.ylabel('Potrošnja (mpg)')


mpg_min = np.min(mpg)
mpg_max = np.max(mpg)
mpg_sr = np.mean(mpg)
print(f"Minimalna potrosnja : {mpg_min}")
print(f"Maksimalna potrosnja : {mpg_max}")
print(f"Srednja potrosnja : {mpg_sr}")

print(data)
print('\n')
plt.show()

datacyl6 = data[data[:,3] == 6]
mpgcyl6=datacyl6[:,0]
hpcyl6=datacyl6[:,3]

print('\n')

mpg_mincyl6 = np.min(mpgcyl6)
mpg_maxcyl6 = np.max(mpgcyl6)
mpg_srcyl6 = np.mean(mpgcyl6)
print(f"Minimalna potrosnja : {mpg_mincyl6}")
print(f"Maksimalna potrosnja : {mpg_maxcyl6}")
print(f"Srednja potrosnja : {mpg_srcyl6}")

plt.figure()
plt.scatter(hpcyl6,mpgcyl6)
plt.xlabel('Konjske snage cyl6')
plt.ylabel('Potrosnja cyl 6')



plt.show()
