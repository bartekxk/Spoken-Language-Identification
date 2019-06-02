#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense, BatchNormalization
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.losses import categorical_crossentropy
from keras.optimizers import Adam
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import tensorflow as tf

train_path = 'spectograms/train50'
test_path = 'spectograms/test50'

train_batches = ImageDataGenerator(rescale=1./255,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True).flow_from_directory(train_path, batch_size=128, target_size=(128, 128))
valid_batches = ImageDataGenerator(rescale=1./255,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True).flow_from_directory(test_path, batch_size=8, target_size=(128, 128))




model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(128, 128, 3)),
    MaxPooling2D(pool_size=(2,2)),
    BatchNormalization(),

    Conv2D(64, kernel_size=(3,3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    BatchNormalization(),

    Conv2D(64, kernel_size=(3,3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    BatchNormalization(),

    Conv2D(96, kernel_size=(3,3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    BatchNormalization(),

    Conv2D(32, kernel_size=(3,3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    BatchNormalization(),
    Dropout(0.2),

    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(3, activation='softmax')
])

model.compile(Adam(lr=.0001), loss='categorical_crossentropy', metrics=['accuracy'])
model.fit_generator(train_batches, steps_per_epoch=100, validation_data=valid_batches, validation_steps=20, epochs=16, verbose=2)
print('saving the model to h5 file...')
model.save('model_2.h5')





# 
# 

# model = Sequential()
# model.add(Conv2D(32, (2, 2), input_shape=(40,40,3))) 
# model.add(Activation('relu')) 
# model.add(MaxPooling2D(pool_size=(2, 2))) 
#   
# model.add(Conv2D(32, (2, 2))) 
# model.add(Activation('relu')) 
# model.add(MaxPooling2D(pool_size=(2, 2))) 
#   
# model.add(Conv2D(64, (2, 2))) 
# model.add(Activation('relu')) 
# model.add(MaxPooling2D(pool_size=(2, 2))) 
# 
# model.add(Dropout(0.25))
# model.add(Flatten())
# model.add(Dense(64, activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(3, activation='softmax'))
# #Compile
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# print(model.summary())
# 
# 
# 
# 
# 
# 
# # TRAINING
# 
# model.fit_generator(
#         train_batches,
#         steps_per_epoch=73080//128,
#         epochs=10,
#         verbose=1,
#         validation_data=test_batches,
#         validation_steps=540//8)
# 
# model.save_weights('10_epochs_50dpi.h5')

# In[ ]:



