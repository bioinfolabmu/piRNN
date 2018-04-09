#2017-01-03
#Kai Wang
#usage: python 4_generate_model.py

#import packages
import pandas
import numpy as np
from keras.utils import np_utils
from keras.utils.np_utils import to_categorical
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

#load the npy data
x_train = np.load('X_train.npy')
y_train = np.load('Y_train.npy')

x_test = np.load('X_test.npy')
y_test = np.load('Y_test.npy')
# change the label into One-hot vector
X_train = np.zeros(shape=(len(x_train),4,341,1))
Y_train = np_utils.to_categorical(y_train,2)

X_test = np.zeros(shape=(len(x_test),4,341,1))
Y_test = np_utils.to_categorical(y_test,2)
#reform the vector into a 4 x 341 matrix
for i in range(len(x_train)):
	tp = np.asarray(x_train[i])
	tp = np.resize(tp,(4,341,1))
	X_train[i] = tp

for i in range(len(x_test)):
	tp = np.asarray(x_test[i])
	tp = np.resize(tp,(4,341,1))
	X_test[i] = tp
# parameters for cnn training
rows, cols = 4, 341

nb_filters = 32

pool_size = (2, 2)

kernel_size = (2, 2)

X_train = X_train.reshape(X_train.shape[0], rows, cols, 1)
X_test = X_test.reshape(X_test.shape[0], rows, cols, 1)


model = Sequential()
model.add(Conv2D(nb_filters, (kernel_size[0],kernel_size[1]), padding='valid',input_shape=input_shape))
model.add(Activation('relu'))
model.add(Conv2D(nb_filters, (kernel_size[0],kernel_size[1])))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=pool_size))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(2))
model.add(Activation('softmax'))
model.compile(loss='binary_crossentropy',
			optimizer='Adam',metrics=['accuracy'])
callbacks = [EarlyStopping(monitor='val_loss',patience=10,verbose=0),ModelCheckpoint(kf_weights_path,monitor='val_loss',save_best_only=True,verbose=0)]
model.fit(x=X_train,y=Y_train, validation_data=(X_test,Y_test), batch_size=32, epochs=150, callbacks=callbacks,verbose=1)

score = model.evaluate(X_test, Y_test, verbose = 0)
print('Test Score: ', score[0])
print('Test Accur: ', score[1])
model.save('model.h5') # the model will be saved into "model.h5" file

