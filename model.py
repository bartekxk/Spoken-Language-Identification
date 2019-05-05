#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import glob
import pandas as pd
import numpy
import numpy as np


def load_data(path):
    x = []
    y = []
    length = len([filename for filename in glob.glob(os.path.join(path, '*.csv'))])
    progress = 0
    for filename in glob.glob(os.path.join(path, '*.csv')):
        label = os.path.split(filename)[1]
        label = label[:2]
        if (label == "en"):
            y.append(0)
        elif (label == "de"):
            y.append(1)
        else:
            y.append(2)
        x.append(numpy.loadtxt(filename))
        progress += 1
        if (progress % 100 == 0):
            print(str(progress) + "/" + str(length))
    print(y)
    return np.stack(x), y


X_train, Y_train = load_data("MFCCtrain")
X_test, Y_test = load_data("MFCCtest")

# import tensorflow as tf
##from keras.models import Sequential
# from keras.layers import Dense
from keras.utils import to_categorical

Y_test = to_categorical(Y_test)
Y_train = to_categorical(Y_train)
# model = Sequential()

# model.add(Dense(10, input_dim=12, activation='relu'))
# model.add(Dense(8, activation='relu'))
# model.add(Dense(3, activation='softmax'))
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=250, batch_size=32)

import tflearn
#import tensorflow as tf

learning_rate = 0.0001
training_iters = 300000  # steps
batch_size = 64

width = 13  # mfcc features
height = 1  # (max) length of utterance
classes = 3  # digits

# Network building
net = tflearn.input_data([None, width, height])
net = tflearn.lstm(net, 128, dropout=0.8)
net = tflearn.fully_connected(net, classes, activation='softmax')
net = tflearn.regression(net, optimizer='adam', learning_rate=learning_rate, loss='categorical_crossentropy')
# Training
# col = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES)
# for x in col:
#    tf.add_to_collection(tf.GraphKeys.VARIABLES, x )

model = tflearn.DNN(net)

model.fit(X_train, Y_train, n_epoch=10, validation_set=(X_test, Y_test), show_metric=True,
          batch_size=64)
_y = model.predict(X)
model.save("tflearn.lstm.model")

# In[39]:


model.save('my_model.h5')

# In[ ]:




