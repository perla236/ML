import numpy as np
import matplotlib.pyplot as plt
from PIL import Image



img = plt.imread("tiger.png")
img = img[:,:,0].copy()
print(img.shape)
print(img.dtype)

imgimg = img.copy()
red,stup = imgimg.shape
if imgimg == 1:
        imgimg=1
for i in range (red):
    
        
    else:
        for j in range (stup):
            imgimg[i][j] += 0.4


#img = np.rot90(img)
#img = np.flip(img, axis=1)
#img = img[::10, ::10]
#width = img.shape[1]
#img[:, :width//2] = 0


plt.imshow(imgimg, cmap='gray')
plt.show()