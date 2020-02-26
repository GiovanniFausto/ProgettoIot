import numpy as np
import imageio as io
import os
path='../ProgettoIot/Progetto/KMeans/'

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
    print('dimensione ricostruita:  ',info.st_size/1024,'KB')


for i in range(8,72,8):#cluster
    for j in range(5,55,5):#iterazioni
        print('cluster: ',i,' iterazionie: ',j)
        ricostruzione(i,j)
       