import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


mtcars = pd.read_csv('mtcars.csv')
print(mtcars)

mtcars.groupby('cyl')['mpg'].mean().plot.bar()

mtcars.boxplot(by='cyl', column='wt')

mtcars.boxplot(by='am', column='mpg')

mtcars.plot.scatter(x = 'qsec', y='hp', c ='am', colormap='inferno')

plt.show()