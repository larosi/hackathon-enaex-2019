# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 12:37:11 2019

@author: Mico
"""


import numpy as np
import matplotlib.pyplot as plt
#import sklearn.metrics as metrics


from keras.layers import Dense
from keras.layers.normalization import BatchNormalization

from keras.models import Sequential
from keras.callbacks import History 
from keras import optimizers



train_test_data = 'train_test_data.npy'
model_name = 'nn_model.h5'
n_neurons = 25
n_epochs = 150
lrate = 0.001

# cargar datos

x_train, x_test, y_train, y_test = np.load(train_test_data)


# parametros de la NN
n_inputs = x_train.shape[1] # tamaño de los features - entrada NN
n_outputs = y_train.shape[1] # salida NN
n_samples = x_train.shape[0]



hist = History()

model = Sequential()

model.add(BatchNormalization())
model.add(Dense(n_neurons*10, activation='relu', input_dim = n_inputs, bias_initializer='zeros'))

model.add(Dense(n_neurons, activation='relu', bias_initializer='zeros'))
model.add(Dense(n_neurons, activation='relu', bias_initializer='zeros'))

model.add(Dense(n_outputs, activation='linear', bias_initializer='zeros'))


#adam optimizer
optimizer = optimizers.Adam(lr=lrate, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
#optimizer = optimizers.SGD(lr=0.01, momentum=0.0, decay=0.0, nesterov=False)
model.compile(optimizer=optimizer, 
              loss='mse', 
              metrics=['mse','mae'])

model.fit(x_train, y_train, epochs = n_epochs, validation_split = 0, callbacks = [hist])
model.save(model_name)

plt.plot(hist.history['loss'])
plt.show()
