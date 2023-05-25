from sklearn import datasets
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
def generate_data(n_samples, flagc):
    
    if flagc == 1:
        random_state = 365
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        
    elif flagc == 2:
        random_state = 148
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)
        
    elif flagc == 3:
        random_state = 148
        X, y = datasets.make_blobs(n_samples=n_samples,
                                    centers=4,
                                    cluster_std=[1.0, 2.5, 0.5, 3.0],
                                    random_state=random_state)

    elif flagc == 4:
        X, y = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)
        
    elif flagc == 5:
        X, y = datasets.make_moons(n_samples=n_samples, noise=.05)
    
    else:
        X = []
        
    return X

x = generate_data(500, 1)
'''plt.figure()
plt.scatter(x[:,0], x[:,1])
plt.show()

KMeans = KMeans(n_clusters= 3)
KMeans.fit(x)
plt.scatter(x[:,0], x[:,1], c=KMeans.labels_)
plt.scatter(KMeans.cluster_centers_[:,0], KMeans.cluster_centers_[:,1], c = 'red')
plt.show()'''

inercija =[]
for i in range (2, 20):
    model = KMeans(n_clusters = i)
    model.fit(x)
    inercija.append(model.inertia_)

plt.figure()
plt.xlabel("klaster")
plt.ylabel("inercija")
plt.plot(inercija, 'b-o')
plt.show()