from skimage import io
from sklearn.cluster import KMeans
import numpy as np 

image=io.imread('tiger.png')
print(image.shape)

rows,cols=image.shape[0],image.shape[1]
print(rows,cols)

image=image.reshape(rows*cols,3)
print(image.shape)

'''n_init : int, default=10
        Number of time the k-means algorithm will be run with different
        centroid seeds. The final results will be the best output of
        n_init consecutive runs in terms of inertia.

    max_iter : int, default=300
        Maximum number of iterations of the k-means algorithm for a
        single run.'''

kmeans = KMeans(n_clusters=24,n_init=3,max_iter=50,verbose=0)

kmeans.fit(image)

print(kmeans.cluster_centers_)

clusters= np.asarray(kmeans.cluster_centers_,dtype=np.uint8)
labels=np.asarray(kmeans.labels_,dtype=np.uint8)
labels=labels.reshape(rows,cols)

np.save('codebook_tiger.npy',clusters)
io.imsave('compressed_tiger.png',labels)


centers=np.load('codebook_tiger.npy')#contiene informazioni sui colori ogni riga è un colore
#print(centers)
c_image=io.imread('compressed_tiger.png') # è formata da numeri che vanno da 0 fino al max numero di cluster
#print(c_image)
image=np.zeros((rows,cols,3),dtype=np.uint8)

for i in range(rows):
    for j in range(cols):
        image[i,j,:]=centers[c_image[i,j],:]#prendendo nella c_image un pixel che ha un valore da 0 a k e con questo prendo una riga di centers che ha il colore

io.imsave('tigrericostruita.png',image)
