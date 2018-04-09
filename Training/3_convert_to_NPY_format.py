#2017-01-03
#Kai Wang
#usage: python 3_convert_to_NPY_format.py

import numpy
import pandas

#####################################################
dataframe = pandas.read_csv("valid.csv", header=None)
dataset = dataframe.values
X = dataset[:,0:1364].astype(float)
Y = dataset[:,1364]

numpy.save('X_valid.npy',X)
numpy.save('Y_valid.npy',Y)

#####################################################

dataframe = pandas.read_csv("train.csv", header=None)
dataset = dataframe.values
X = dataset[:,0:1364].astype(float)
Y = dataset[:,1364]

numpy.save('X_train.npy',X)
numpy.save('Y_train.npy',Y_tr)

####################################################

dataframe = pandas.read_csv("test.csv", header=None)
dataset = dataframe.values
X = dataset[:,0:1364].astype(float)
Y = dataset[:,1364]

numpy.save('X_test.npy',X)
numpy.save('Y_test.npy',Y)