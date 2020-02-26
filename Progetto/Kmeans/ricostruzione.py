import numpy as np 
from skimage import io
import os

path='../ProgettoIot/Progetto/KMeans/'


def decompress(ncluster,maxiter):
    dest=path+str(ncluster)+'_cluster'
    centers=np.load(dest+'/codebook_tiger'+str(maxiter) +'_iter.npy')#contiene informazioni sui colori ogni riga è un colore
    c_image=io.imread(dest+'/compressed_tiger'+str(maxiter)+'_iter.png')# è formata da numeri che vanno da 0 fino al max numero di cluster
    info = os.stat(path+'tiger.png')
    print("Dimensione prima dell'algoritmo K-mean: ",info.st_size/1024,"KB")
    image = np.zeros((c_image.shape[0],c_image.shape[1],3),dtype=np.uint8 )
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i,j,:]=centers[c_image[i,j],:]#prendendo nella c_image un pixel che ha un valore da 0 a k e con questo prendo una riga di centers che ha il colore
    io.imsave(dest+'/tigrericostruita'+str(maxiter)+'_iter.png',image)
    info = os.stat(dest+'/tigrericostruita'+str(maxiter)+'_iter.png')
    print("Dimensione dopo l'algoritmo K-mean: ",info.st_size/1024,"KB")

for i in range(8,72,8):#cluster
    for j in range(5,55,5):#iterazioni
        print('cluster: ',i,' iterazionie: ',j)
        decompress(i,j)
