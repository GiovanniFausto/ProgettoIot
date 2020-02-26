from skimage import io
from sklearn.cluster import KMeans
import numpy as np 
from pathlib import Path

path='../ProgettoIot/Progetto/KMeans/'

image=io.imread(path+'tiger.png')
rows,cols=image.shape[0],image.shape[1]
image=image.reshape(rows*cols,3)


def process(ncluster,maxiter):
    kmeans = KMeans(n_clusters=ncluster,n_init=1,max_iter=maxiter,verbose=0)
    kmeans.fit(image)
    clusters= np.asarray(kmeans.cluster_centers_,dtype=np.uint8)#in pratica li porta in int sono i centri
    labels=np.asarray(kmeans.labels_,dtype=np.uint8)#li mette come arrai
    labels=labels.reshape(rows,cols)#li porta a matrice 
    dest=path+str(ncluster)+'_cluster' #crea la cartella col numero di cluster
    Path(dest).mkdir(parents=True, exist_ok=True)
    np.save(dest+'/codebook_tiger'+str(maxiter) +'_iter.npy',clusters)
    io.imsave(dest+'/compressed_tiger'+str(maxiter)+'_iter.png',labels)

for i in range(8,64,8):#cluster
    for j in range(5,50,5):#iterazioni
        print(i,j)
        process(i,j)
        





