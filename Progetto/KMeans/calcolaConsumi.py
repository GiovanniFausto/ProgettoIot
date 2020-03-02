import matplotlib.pyplot as plt
import csv
import numpy as np
import os



#lorawanmin=24 #mA
#lorawanmax=44 
lorawandataratemin=250 #bit/s
lorawandataratemax=50000

#nbiotmin=74
#nbiotmax=220
nbiotdataremin=66000
nbiotdataremax=160000


path='../ProgettoIot/Progetto/KMeans/'

x=[]
y=[]
z=[]


dati={}
tempiloramin=[]
tempiloramax=[]
tempinbmin=[]
tempinbmax=[]
'''
consumiloramin=[]
consumiloramax=[]
consuminbmin=[]
consuminbmax=[]
'''


with open(path+'dati/dimensioninere.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))#num cluster
        y.append(int(row[1]))#iterazion
        z.append(float(row[2]))
        dati[str(row[0])]=float(row[2])*8192 #immagine in bit


#print(dati)
info=os.stat(path+'tiger.png')#serve per prendere la dimensione e salvarla

dati['origina']=(info.st_size/1024)*8192



for x in dati:
    tempiloramax.append(dati[x]/lorawandataratemin)# il tempo è massimo quando il data rate è minimo consumo meno potenzaa è in SECONDI
    tempiloramin.append(dati[x]/lorawandataratemax)

for x in dati:
    tempinbmax.append(dati[x]/nbiotdataremin)# il tempo è massimo quando il data rate è minimo consumo meno potenzaa
    tempinbmin.append(dati[x]/nbiotdataremax)# il tempo è minimo se trasmettiamo a data rate alti

tempiloramin=[int(i) for i in tempiloramin]
tempiloramax=[int(i) for i in tempiloramax]
tempinbmax=[int(i) for i in tempinbmax]
tempinbmin=[int(i) for i in tempinbmin]



print(tempiloramin,tempiloramax)
print('\n')
print(tempinbmin,tempinbmax)

info=os.stat(path+'tiger.png')#serve per prendere la dimensione e salvarla
print(info.st_size/1024)

plt.plot(x, z, label= "stars", color= "blue",marker='o') 
#plt.plot(x1, z1, label= "stars", color= "red",marker='+') 
#plt.plot(x2, z2, label= "stars", color= "green",marker='*') 


#iter50 = plt.Line2D([], [], color='blue', marker='o',markersize=5, label='40 iterazioni')
#iter5 = plt.Line2D([], [], color='red', marker='+',markersize=15, label='5 iterazioni')
#iter25 = plt.Line2D([], [], color='green', marker='*',markersize=15, label='25 iterazioni')
#plt.legend(handles=[iter5,iter25,iter50])

plt.title('Dati immagini contenenti etichette')
plt.xlabel('Cluster')
plt.ylabel('KB')

plt.xticks(np.arange(0, 72, 8)) 
plt.yticks(np.arange(100, 400, 50)) 

plt.show()







'''
print(tempiloramin,tempiloramax)
print('\n')
print(tempinbmin,tempinbmax)
'''
#nb più veloce ci sta meno tempo
'''
consumiloramin=np.array(tempiloramax)*lorawanmin
consumiloramax=np.array(tempiloramin)*lorawanmax
consuminbmin=np.array(tempinbmax)*nbiotmin
consuminbmax=np.array(tempinbmin)*nbiotmax
print('\nloramin',consumiloramin,'\nloramx',consumiloramax,'\nnbmin',consuminbmin,'\nnbmax',consuminbmax)


'''
'''
    
plt.plot(x, z, label= "stars", color= "blue",marker='o') 
#plt.plot(x1, z1, label= "stars", color= "red",marker='+') 
#plt.plot(x2, z2, label= "stars", color= "green",marker='*') 


#iter50 = plt.Line2D([], [], color='blue', marker='o',markersize=5, label='40 iterazioni')
#iter5 = plt.Line2D([], [], color='red', marker='+',markersize=15, label='5 iterazioni')
#iter25 = plt.Line2D([], [], color='green', marker='*',markersize=15, label='25 iterazioni')
#plt.legend(handles=[iter5,iter25,iter50])

plt.title('Dati immagini contenenti etichette')
plt.xlabel('Cluster')
plt.ylabel('KB')

plt.xticks(np.arange(0, 72, 8)) 
plt.yticks(np.arange(100, 400, 50)) 

plt.show()'''