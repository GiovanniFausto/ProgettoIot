from skimage import io
from sklearn.cluster import KMeans
import numpy as np 
from pathlib import Path
import time
import csv

path='../ProgettoIot/Progetto/KMeans/' 

image=io.imread(path+'tiger.png') # prende l'immagine principale
rows,cols=image.shape[0],image.shape[1]#prende righe e colonne

image=image.reshape(rows*cols,3)# la porta in un'unica vettore
tempi={} #per salvare i tempi di esecuzione

#seleziono i valori del test
numCluster=24
numIter=20

# per i vari casi di kmeans
def process(ncluster,maxiter):

    tmp1=time.time()

    kmeans = KMeans(n_clusters=ncluster,n_init=1,max_iter=maxiter,verbose=0)
    kmeans.fit(image)

    tmp=time.time()-tmp1#calcolo il tempo di esecuzione

    key=str(ncluster)+'_'+str(maxiter)# crea le chiavi per i tempi clu_iter
    tempi[str(key)]=tmp #ho i tempi delle varie esecuzioni
    
    clusters= np.asarray(kmeans.cluster_centers_,dtype=np.uint8)#in pratica li porta in int sono i centri
    labels=np.asarray(kmeans.labels_,dtype=np.uint8)#li mette come arrai
    labels=labels.reshape(rows,cols)#li porta a matrice 

    dest=path+str(ncluster)+'_cluster' #crea la cartella col numero di cluster
    Path(dest).mkdir(parents=True, exist_ok=True)


    np.save(dest+'/codebook_tiger'+str(maxiter) +'_iter.npy',clusters)#salva l'immagine e i dati per la ricostruzione
    io.imsave(dest+'/compressed_tiger'+str(maxiter)+'_iter.png',labels)

#per calcolare il kmeans
for i in range(8,numCluster,8):#cluster
    for j in range(5,numIter,5):#iterazioni
        #print('cluster: ',i,' iterazionie: ',j)
        process(i,j)
        #print(tempi)#mette i tempi di ogni esecuzione
        

dest=path+'dati'
Path(dest).mkdir(parents=True, exist_ok=True)
#per scrivere i tempi in csv
with open(path+'/dati/tempi.csv', 'w', newline="") as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in tempi.items():
       writer.writerow([key, value])


