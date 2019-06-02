#!/usr/bin/env python
# coding: utf-8

# In[2]:


import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
import os
import glob

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()


path = "spoken-language-identification/train/" #training data path
resultsDir= "spectograms/train50" #create mentioned dir
length = len([filename for filename in glob.glob(os.path.join(path, '*.flac'))])

printProgressBar(0, length, prefix = 'Progress:', suffix = 'Complete', length = 50)
it=0
for filename in glob.glob(os.path.join(path, '*.flac')):
    #processing outputname
    outputFile = os.path.split(filename)[1]
    label = outputFile[:2]
    if label == 'en':
        label = 'english/'
    elif label == 'de':
        label = 'german/'
    elif label == 'es':
        label = 'spanish/'
   
    outputFile = resultsDir + "/" + label + os.path.splitext(outputFile)[0] +".png"
    #reading data
    data, samplerate = sf.read(filename)
    fig,ax = plt.subplots(1)
    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    ax.axis('off')
    #processing data
    pxx, freqs, t, im = ax.specgram(x=data, Fs=samplerate, NFFT=512)
    ax.axis('off')
    fig.savefig(outputFile, dpi=50, frameon='false')
    plt.close('all')
    it += 1
    printProgressBar(it, length, prefix = 'Progress:', suffix = 'Complete', length = 50)
  


# In[ ]:





# In[ ]:



