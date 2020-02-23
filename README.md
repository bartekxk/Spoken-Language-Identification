# Spoken Language Identification
Jakub Lewkowicz, Bartłomiej Kocot

## Introduction
The goal of our project was to create an application that classifies spoken language based on recording through a microphone or upload a recording file. In our project we have included three languages, i.e. English, German and Spanish, and created a model that defines one of the classes listed for a given recording. Our solution is based on processing 10-second audio recordings in the .flac format into spectrograms, which are then processed by a revolutionary neural network that returns the probability of belonging to a given class. In order to implement the network, we used the Keras library. The data set we used was downloaded from the kaggle platform https://www.kaggle.com/toponowicz/spoken-language-identification . 

## Tasks
Find appropriate dataset, processing of sound files, choosing the right model, training the model, testing the model, and comparing the results obtained in other models, creating an application using the already trained model.

## Data set
The data set consists of 73080 training files and 540 validation files. Recordings are in .flac format and each is 10 seconds long. In the collection, the samples are evenly distributed in terms of language, gender, sound distortions as well as the speaker's accent.

## KNN algorithm
The first approach to the project was to use the knn algorithm from previously generated sound features by the MFCC algorithm. We created our own knn algorithm, and then due to the large number of features per sound file (around 2000) we had to reduce them accordingly. Unfortunately, the algorithm gave effects up to 48%. It can be concluded that the KNN algorithm is not suitable for large amounts of data, and their reduction can result in the loss of important information.

## Model

This solution was created on the basis of other examples of solutions for similar problems found on the Internet. The initial idea was the language classification based on the KNN algorithm, although after a while we came to the conclusion that it does not have the slightest application for such large data (73080 files). The implementation of KNN algorithms is in the file knnAlgorithm.py. The use of CNN has proved to be much more effective, but it is also not the optimal solution. Another solution worth noting is the use of the MFCC algorithm and the use of e.g. LSTM networks. 

## Training

Before we began training our network, we had to convert the sound files into spectrograms (algorithm in the file spectrograms.py). We generated spectrograms in 50 dpi quality, and then before uploading the files to the network we changed their resolution to 128x128 px.

Training Parameters:

optimizer: Adam,

training_batch_size: 128,

validation_batch_size: 8,

loss = 'categorical_crossentropy'

steps_per_epoch = 200,

validation_steps = 50,

epochs = 30

 

For these parameters, we obtained 65% efficiency for validation data and 85% for training data. Earlier using similar parameters, but generating spectrograms with a quality of 10 dpi (converting them to 40x40 px), we obtained an efficiency of about 50%, so we can assume that to some extent for better quality you can get much better results. However, better quality is associated with significantly longer processing time for both spectrogram generation and network training. 

## Graphic interface

In order to visualize our work, we have created a graphical application interface. It makes it possible to identify a language based on an audio file or "live" recording. When recording, the sound file is saved in the temporary folder. In both methods, an appropriate spectogram is then created and the application returns the appropriate language based on its and the model created. To create the graphical interface we used Qt for Python (PySide2 library).
