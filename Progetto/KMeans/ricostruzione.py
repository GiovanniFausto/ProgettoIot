import numpy as np
import imageio as io
import os
import csv


path='../ProgettoIot/Progetto/KMeans/'
dimensioni={}

numCluster=72
numIter=55

def ricostruzione(cluster,iterazioni):
    srccb=path+str(cluster)+'_cluster/codebook_tiger'+str(iterazioni)+'_iter.npy'
    srcim=path+str(cluster)+'_cluster/compressed_tiger'+str(iterazioni)+'_iter.png'
    centers=np.load(srccb)#contiene informazioni sui colori ogni riga è un colore
    c_image=io.imread(srcim) # è formata da numeri che vanno da 0 fino al max numero di cluster
    rows,cols=c_image.shape[0],c_image.shape[1]
    image=np.zeros((rows,cols,3),dtype=np.uint8)

    for i in range(rows):
        for j in range(cols):
            image[i,j,:]=centers[c_image[i,j],:]#prendendo nella c_image un pixel che ha un valore da 0 a k e con questo prendo una riga di centers che ha il colore

    dest=path+str(cluster)+'_'+str(iterazioni)+'_tigrericostruita.png'
    io.imsave(dest,image)
    info=os.stat(dest)

    key=str(cluster)+'_'+str(iterazioni)# crea le chiavi per i tempi
    dimensioni[str(key)]=info.st_size/1024 #ho i tempi delle varie esecuzioni

    print('dimensione ricostruita:  ',info.st_size/1024,'KB')


#per ricostruire le immagini
for i in range(8,numCluster,8):#cluster
    for j in range(5,numIter,5):#iterazioni
        print('cluster: ',i,' iterazionie: ',j)
        ricostruzione(i,j)
        print(dimensioni)
       
#per salvare i dati in csv
with open(path+'/dimensioni.csv', 'w', newline="") as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in dimensioni.items():
       writer.writerow([key, value])