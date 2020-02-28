import cv2
import csv
from pathlib import Path
from skimage.metrics import structural_similarity as ssim

numCluster=72
numIter=55

path='../ProgettoIot/Progetto/KMeans/'
ssimdati={}

def cssim(image1,image2,i,j):
    s=ssim(img1,img2, multichannel=True)#calcola il psnr dell'immagine di partenza con quella ricostruita
    #print(psnr)
    key=str(i)
    key2=str(j)
    ssimdati[str(key),str(key2)]=s #aggiungo i psnr per poi salvarli


img1=cv2.imread(path+'tiger.png')

for i in range(8,numCluster,8):#cluster
    for j in range(5,numIter,5):#iterazioni
        src=path+'ricostruzione/'+str(i)+'_'+str(j)+'_tigrericostruita.png'
        img2=cv2.imread(src)
        #print('cluster: ',i,' iterazionie: ',j)
        #print(src)
        cssim(img1,img2,i,j)
        #print(psnrdati)


dest=path+'dati'
Path(dest).mkdir(parents=True, exist_ok=True)
with open(path+'/dati/ssim.csv', 'w', newline="") as csv_file:  
    writer = csv.writer(csv_file)
    for [key,key2], value in ssimdati.items():
       writer.writerow([key,key2, value])

