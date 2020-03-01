import matplotlib.pyplot as plt
import csv
import numpy as np



lorawanmin=24 #mA
lorawanmax=44 
lorawandataratemin=250 #bit/s
lorawandataratemax=50000

nbiotmin=74
nbiotmax=220
nbiotdataremin=66000
nbiotdataremax=160000


path='../ProgettoIot/Progetto/KMeans/dati/'

x=[]
y=[]
z=[]


dati={}
tempiloramin=[]
tempiloramax=[]
tempinbmin=[]
tempinbmax=[]

consumiloramin=[]
consumiloramax=[]
consuminbmin=[]
consuminbmax=[]



with open(path+'dimensioninere.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))#num cluster
        y.append(int(row[1]))#iterazion
        z.append(float(row[2]))
        dati[str(row[0])]=float(row[2])*8192


#print(dati)

for x in dati:
    tempiloramax.append(dati[x]/lorawandataratemax)
    tempiloramin.append(dati[x]/lorawandataratemin)

for x in dati:
    tempinbmax.append(dati[x]/nbiotdataremax)
    tempinbmin.append(dati[x]/nbiotdataremin)


print(tempiloramin,tempiloramax)
print('\n')
print(tempinbmin,tempinbmax)

#nb più veloce ci sta meno tempo

consumiloramin=np.array(tempiloramin)*lorawanmin
consumiloramax=np.array(tempiloramax)*lorawanmax
consuminbmin=np.array(tempinbmin)*nbiotmax
consuminbmax=np.array(tempinbmax)*nbiotmin
print(consumiloramin,consumiloramax,consuminbmin,consuminbmax)



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