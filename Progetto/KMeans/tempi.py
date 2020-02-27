import matplotlib.pyplot as plt
import csv

path='../ProgettoIot/Progetto/KMeans/dati/'

x=[]
y=[]
z=[]

with open(path+'tempi.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
            x.append(int(row[0]))
            y.append(int(row[1]))
            z.append(float(row[2]))
       

plt.plot(x,z, marker='o')
plt.title('Data from the CSV File')
plt.xlabel('cluster')
plt.ylabel('sec')

plt.show()