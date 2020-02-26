from skimage import io
from sklearn.cluster import KMeans
import numpy as np 
from pathlib import Path
import time
import csv

path='../ProgettoIot/Progetto/KMeans/'

image=io.imread(path+'tiger.png')
rows,cols=image.shape[0],image.shape[1]

print(rows)

image=image.reshape(rows*cols,3)
tempi={}

def process(ncluster,maxiter):

    tmp1=time.time()
    kmeans = KMeans(n_clusters=ncluster,n_init=1,max_iter=maxiter,verbose=0)
    kmeans.fit(image)
    tmp=time.time()-tmp1

    key=str(ncluster)+'_'+str(maxiter)# crea le chiavi per i tempi
    tempi[str(key)]=tmp #ho i tempi delle varie esecuzioni
    
    clusters= np.asarray(kmeans.cluster_centers_,dtype=np.uint8)#in pratica li porta in int sono i centri
    labels=np.asarray(kmeans.labels_,dtype=np.uint8)#li mette come arrai
    labels=labels.reshape(rows,cols)#li porta a matrice 
    dest=path+str(ncluster)+'_cluster' #crea la cartella col numero di cluster
    Path(dest).mkdir(parents=True, exist_ok=True)
    np.save(dest+'/codebook_tiger'+str(maxiter) +'_iter.npy',clusters)
    io.imsave(dest+'/compressed_tiger'+str(maxiter)+'_iter.png',labels)

for i in range(8,72,8):#cluster
    for j in range(5,55,5):#iterazioni
        print('cluster: ',i,' iterazionie: ',j)
        process(i,j)
        print(tempi)#mette i tempi di ogni esecuzione
        


with open(path+'/tempi.csv', 'w', newline="") as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in tempi.items():
       writer.writerow([key, value])