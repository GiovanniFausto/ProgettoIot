import matplotlib.pyplot as plt
import csv
import numpy as np

path='../ProgettoIot/Progetto/KMeans/dati/'

x=[]
y=[]
z=[]
x1=[]
y1=[]
z1=[]
x2=[]
y2=[]
z2=[]

with open(path+'psnr.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        if int(row[1])==40: #con 40 iter
            x.append(int(row[0]))#num cluster
            y.append(int(row[1]))#iterazion
            z.append(float(row[2]))#tempi
        if int(row[1])==5:#con 5 iter
            x1.append(int(row[0]))#num cluster
            y1.append(int(row[1]))#iterazion
            z1.append(float(row[2]))#tempi
        if int(row[1])==25:#con 25 iter
            x2.append(int(row[0]))#num cluster
            y2.append(int(row[1]))#iterazion
            z2.append(float(row[2]))#tempi


plt.plot(x, z, label= "stars", color= "blue",marker='o') 
plt.plot(x1, z1, label= "stars", color= "red",marker='+') 
plt.plot(x2, z2, label= "stars", color= "green",marker='*') 


iter50 = plt.Line2D([], [], color='blue', marker='o',markersize=5, label='40 iterazioni')
iter5 = plt.Line2D([], [], color='red', marker='+',markersize=15, label='5 iterazioni')
iter25 = plt.Line2D([], [], color='green', marker='*',markersize=15, label='25 iterazioni')
plt.legend(handles=[iter5,iter25,iter50])

plt.title('Dati dal file psnr.csv')
plt.xlabel('Cluster')
plt.ylabel('PSNR')

plt.xticks(np.arange(0, 72, 8)) 
plt.yticks(np.arange(22, 34, 1)) 

plt.show()