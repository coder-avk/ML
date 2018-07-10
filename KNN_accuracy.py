import numpy as np
from mnist import MNIST
import struct
import os
mndata = MNIST('/home/oslab/avk/')
images , labels = mndata.load_training()
data_train = np.array(images)
data_labels = np.array(labels) 
test_data , test_labels = mndata.load_testing()
test_data = np.array(test_data)
test_labels = np.array(test_labels)
correct = 0
for j in range(0,10000):
    small = 1000000.4654
    for i in range(0,60000):
        dist = np.linalg.norm(data_train[i]-test_data[j])
        if dist<small:
            index = i
            small = dist
    if data_labels[index]==test_labels[j]:
        correct = correct + 1
acc = correct /60000.0
print("Accuracy = "+str(acc)+" %")
