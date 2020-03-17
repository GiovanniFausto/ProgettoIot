import cv2
import csv
from pathlib import Path

numCluster=72
numIter=55

path='../ProgettoIot/Progetto/KMeans/'
psnrdati={}

def cpsnr(image1,image2,i,j):
    psnr=cv2.PSNR(img1,img2)#calcola il psnr dell'immagine di partenza con quella ricostruita
    #print(psnr)
    key=str(i)
    key2=str(j)
    psnrdati[str(key),str(key2)]=psnr #aggiungo i psnr per poi salvarli


img1=cv2.imread(path+'tiger.png')

for i in range(8,numCluster,8):#cluster
    for j in range(5,numIter,5):#iterazioni
        src=path+'ricostruzione/'+str(i)+'_'+str(j)+'_tigrericostruita.png'
        img2=cv2.imread(src)
        cpsnr(img1,img2,i,j)



dest=path+'dati'
Path(dest).mkdir(parents=True, exist_ok=True)
with open(path+'/dati/psnr.csv', 'w', newline="") as csv_file:  
    writer = csv.writer(csv_file)
    for [key,key2], value in psnrdati.items():
       writer.writerow([key,key2, value])

