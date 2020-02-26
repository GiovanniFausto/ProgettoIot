import cv2

path='../ProgettoIot/Progetto/KMeans/'

img1=cv2.imread(path+'tiger.png')
img2=cv2.imread(path+'8_5_tigrericostruita.png')
psnr=cv2.PSNR(img1,img2)
print(psnr)