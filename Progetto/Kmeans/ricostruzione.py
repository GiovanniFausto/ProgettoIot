import numpy as np 
from skimage import io

centers=np.load('codebook_tiger.npy')#contiene informazioni sui colori ogni riga è un colore
#print(centers)
c_image=io.imread('compressed_tiger.png') # è formata da numeri che vanno da 0 fino al max numero di cluster
#print(c_image)
image=np.zeros((image.shape[0],image.shape[1],3),dtype=np.uint8)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        image[i,j,:]=centers[c_image[i,j],:]#prendendo nella c_image un pixel che ha un valore da 0 a k e con questo prendo una riga di centers che ha il colore

io.imsave('tigrericostruita.png',image)