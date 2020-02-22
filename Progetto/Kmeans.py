from skimage import io
import numpy as np
import numpy.matlib

image = io.imread('tiger.png')
#io.imshow(image)
#io.show()


rows = image.shape[0]
cols = image.shape[1]
image = image/255
X = image.reshape(image.shape[0]*image.shape[1],3)

K = 8 #number of clusters
max_iters = 5 #number of times the k-mean should run

import random
def init_centroids(X,K):
    c = random.sample(list(X),K)
    return c

def closest_centroids(X,c):
    K = np.size(c,0)
    idx = np.zeros((np.size(X,0),1))
    arr = np.empty((np.size(X,0),1))
    for i in range(0,K):
        y = c[i]
        temp = np.ones((np.size(X,0),1))*y
        b = np.power(np.subtract(X,temp),2)
        a = np.sum(b,axis = 1)
        a = np.asarray(a)
        a.resize((np.size(X,0),1))
        #print(np.shape(a))
        arr = np.append(arr, a, axis=1)
    arr = np.delete(arr,0,axis=1)
    idx = np.argmin(arr, axis=1)
    return idx

def compute_centroids(X,idx,K):
    n = np.size(X,1)
    centroids = np.zeros((K,n))
    for i in range(0,K):
        ci = idx==i
        ci = ci.astype(int)
        total_number = sum(ci)
        ci.resize((np.size(X,0),1))
        total_matrix = np.matlib.repmat(ci,1,n)
        ci = np.transpose(ci)
        total = np.multiply(X,total_matrix)
        centroids[i] = (1/total_number)*np.sum(total,axis=0)
    return centroids

def run_kMean(X,initial_centroids,max_iters):
    m = np.size(X,0)
    n = np.size(X,1)
    K = np.size(initial_centroids,0)
    centroids = initial_centroids
    previous_centroids = centroids
    idx = np.zeros((m,1))
    for i in range(1,max_iters,4):
        idx = closest_centroids(X,centroids)
        centroids = compute_centroids(X,idx,K)
    return centroids,idx

import time
tmp1=time.time()

initial_centroids = init_centroids(X,K)
centroids,idx = run_kMean(X,initial_centroids,max_iters)
#idx.resize((np.size(X,0),1))
print(time.time()-tmp1)
print(np.shape(centroids))
print(np.shape(idx))


idx = closest_centroids(X,centroids)
X_recovered = centroids[idx]
print(np.shape(X_recovered))
X_recovered = np.reshape(X_recovered, (rows, cols, 3))
print(np.shape(X_recovered))


import imageio
prova= 'tiger_small'+str(time.localtime().tm_min)+'.jpg'
imageio.imwrite(prova, X_recovered)

image_compressed = io.imread(prova)
#io.imshow(image_compressed)
#io.show()


import os
info = os.stat('tiger.png')
print("size of image before running K-mean algorithm: ",info.st_size/1024,"KB")
info = os.stat(prova)
print("size of image after running K-mean algorithm: ",info.st_size/1024,"KB")