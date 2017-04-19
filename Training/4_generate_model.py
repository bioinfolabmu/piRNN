#2017-01-03
#Kai Wang
#usage: python 4_generate_model.py

#import packages
import pandas
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization, Activation
from keras.optimizers import Adam
from keras.wrappers.scikit_learn import KerasClassifier
from keras.models import load_model
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

X_train = np.load('X_train.npy')
Y_train = np.load('Y_train.npy')

X_test = np.load('X_test.npy')
Y_test = np.load('Y_test.npy')

model = Sequential()
model.add(Dense(512, input_dim = 341, init = 'normal', activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(256, init = 'normal', activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(1, init = 'normal', activation = 'sigmoid'))

opt = Adam()

model.compile(loss = 'binary_crossentropy', optimizer = opt, metrics = ['accuracy'])

model.fit(X_train, Y_train, batch_size = 32, nb_epoch = 55, verbose = 1, validation_data = (X_test, Y_test))

score = model.evaluate(X_test, Y_test, verbose = 0)
print('Test Score: ', score[0])
print('Test Accur: ', score[1])
model.save('model.h5')
