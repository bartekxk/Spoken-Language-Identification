from PySide2 import QtCore, QtGui, QtWidgets
import sys,glob,os
from keras.models import load_model
from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import write
import soundfile as sf
from pydub import AudioSegment
import sounddevice as sd
import tensorflow as tf

class Gui(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.resize(400,400)
        self.setWindowTitle("Spoken Language Identification ")
        self.show()
        self.addLabels()
        self.addButtons()
        self.recording=False
        self.fs=44100
        self.model=load_model("model_2.h5")
        self.clearDirectory()

    def addButtons(self):
        self.selectFileButton = QtWidgets.QPushButton(self)
        self.selectFileButton.setText('Dodaj plik')
        self.selectFileButton.resize(80, 50)
        self.selectFileButton.move(300, 50)
        self.selectFileButton.clicked.connect(self.getInputFile)
        self.selectFileButton.show()
        self.recordButton = QtWidgets.QPushButton(self)
        self.recordButton.setText('Nagrywaj')
        self.recordButton.resize(80,50)
        self.recordButton.move(160,200)
        self.recordButton.clicked.connect(self.record)
        self.recordButton.show()

    def addLabels(self):
        self.file_path_label=QtWidgets.QLabel(self)
        self.file_path_label.setText("")
        self.file_path_label.resize(250,50)
        self.file_path_label.move(50,50)
        self.file_path_label.show()
        self.result_label=QtWidgets.QLabel(self)
        self.result_label.setText("")
        self.result_label.resize(100,50)
        self.result_label.move(150,350)
        self.result_label.show()
    def clearDirectory(self):
        files = glob.glob('./tmp/*')
        for f in files:
            os.remove(f)

    def record (self):
        if self.recording==False:
            self.recordButton.setText("Nagrywanie")
            self.recording=True
            sr = 44100
            duration = 10
            myrecording = sd.rec(int(duration * sr), samplerate=sr, channels=1)
            sd.wait()
            #sd.play(myrecording, sr)
            sf.write("./tmp/record.wav", myrecording, sr)
            self.recording=False
            song = AudioSegment.from_wav("./tmp/record.wav")
            song.export("./tmp/recordf.flac", format="flac")
            self.process("./tmp/recordf.flac")
        #else:
         #   self.recordButton.setText("Nagrywaj")
          #  self.recording=False
    def getInputFile(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self,
                                                     'Open file',
                                                     '/home',
                                                     'All files (*.*)',
                                                     options=QtWidgets.QFileDialog.DontUseNativeDialog)
        self.file_path=filename[0]
        self.file_path_label.setText(self.file_path)
        self.process(self.file_path)

    def spectogram(self,file):
        outputFile =  "./tmp/"+os.path.split(file)[1][:-5]+ ".png"
        # reading data
        data, samplerate = sf.read(file)
        fig, ax = plt.subplots(1)
        fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        ax.axis('off')
        # processing data
        pxx, freqs, t, im = ax.specgram(x=data, Fs=samplerate, NFFT=512)
        ax.axis('off')
        fig.savefig(outputFile, dpi=100, frameon='false')
        plt.close('all')
        return outputFile

    def spectogramtest(self,a):
        outputFile="./tmp/record.png"
        fig, ax = plt.subplots(1)
        fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        ax.axis('off')
        # processing data
        pxx, freqs, t, im = ax.specgram(x=a, Fs=22050, NFFT=512)
        ax.axis('off')
        fig.savefig(outputFile, dpi=100, frameon='false')
        plt.close('all')
        return outputFile

    def load_image(self,img_path, show=False):
        img = image.load_img(img_path, target_size=(128, 128))
        img_tensor = image.img_to_array(img)  # (height, width, channels)
        img_tensor = np.expand_dims(img_tensor,
                                    axis=0)  # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
        img_tensor /= 255.  # imshow expects values in the range [0, 1]
        if show:
            plt.imshow(img_tensor[0])
            plt.axis('off')
            plt.show()

        return img_tensor

    def getLanguage(self,arr):
        if arr[0][0]>arr[0][1]:
            if arr[0][0]>arr[0][2]:
                return "Angielski"
            else:
                return "Niemiecki"
        else:
            if arr[0][1] > arr[0][2]:
                return "Hiszpański"
            else:
                return "Niemiecki"

    def process(self,file):
        path=self.spectogram(file)
        new_image = self.load_image(path)
        pred = self.model.predict(new_image)
        self.result_label.setText(self.getLanguage(pred))
        self.clearDirectory()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui=Gui()
    sys.exit(app.exec_())
