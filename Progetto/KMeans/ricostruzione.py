import numpy as np
import imageio as io
import os
import csv
from pathlib import Path

path='../ProgettoIot/Progetto/KMeans/'
dimensioni={}

numCluster=24
numIter=20

def ricostruzione(cluster,iterazioni):
    srccb=path+str(cluster)+'_cluster/codebook_tiger'+str(iterazioni)+'_iter.npy' # prendo il file con i dati del kmeans i centroidi
    srcim=path+str(cluster)+'_cluster/compressed_tiger'+str(iterazioni)+'_iter.png' # prendo l'immagine dove ci stanno le informazioni

    centers=np.load(srccb)#contiene informazioni sui colori ogni riga è un colore
    c_image=io.imread(srcim) # è formata da numeri che vanno da 0 fino al max numero di cluster

    rows,cols=c_image.shape[0],c_image.shape[1]# prendo la dimensione dell'immagine
    image=np.zeros((rows,cols,3),dtype=np.uint8)

    for i in range(rows):
        for j in range(cols):
            image[i,j,:]=centers[c_image[i,j],:]#prendendo nella c_image un pixel che ha un valore da 0 a k e con questo prendo una riga di centers che ha il colore

    dest=path+'ricostruzione' #creo la cartella ricostruzione se non c'è
    Path(dest).mkdir(parents=True, exist_ok=True)

    dest=path+'ricostruzione/'+str(cluster)+'_'+str(iterazioni)+'_tigrericostruita.png' #creo path dove salvare la nuova immagine
    io.imsave(dest,image)
    info=os.stat(dest)#serve per prendere la dimensione e salvarla

    key=str(cluster)+'_'+str(iterazioni)# crea le chiavi per i tempi
    dimensioni[str(key)]=info.st_size/1024 #ho i tempi delle varie esecuzioni

    #print('dimensione ricostruita:  ',info.st_size/1024,'KB')


#per ricostruire le immagini
for i in range(8,numCluster,8):#cluster
    for j in range(5,numIter,5):#iterazioni
        #print('cluster: ',i,' iterazionie: ',j)
        ricostruzione(i,j)
        #print(dimensioni)


dest=path+'dati' 
Path(dest).mkdir(parents=True, exist_ok=True)

#per salvare i dati in csv
with open(path+'/dati/dimensioni.csv', 'w', newline="") as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in dimensioni.items():
       writer.writerow([key, value])