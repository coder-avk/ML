# this is a python program for KNN algorithm on MNIST dataset for digit recognition

import numpy as np
from mnist import MNIST
import struct
import os

mndata = MNIST('/home/oslab/avk/')
images , labels = mndata.load_training()
data_train = np.array(images)
data_labels = np.array(labels) 

n = input("Enter the row to check which digit is stored in it?")
small = 1000000.4654
for i in range(0,60000):
    dist = np.linalg.norm(data_train[i]-data_train[n])
#     print(dist)
    if dist<small and i!=n:
        small = dist
        index = i
print("The minimum distance = "+str(dist))
print("The digit on the given row is = "+str(data_labels[index]))
