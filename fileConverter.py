import glob,numpy
mfcc_counts=13
file_list = glob.glob("./*")
iterations=0
for file in file_list:
    if file!="./fileConverter.py" and file!="./fileConverter.pyc":
        language = file[2:][:2]
        if language=="de":
            languageNum=1
        if language=="en":
            languageNum=2
        if language=="es":
            languageNum=3
        fileContent=numpy.genfromtxt(file,delimiter=',')
        file=open(file,"w+")
        file.write(str(languageNum)+",")
        for i in range (0,mfcc_counts-1):
            file.write(str(fileContent[i][0])+",")
        file.write(str(fileContent[mfcc_counts-1][0]))
        file.close()
        iterations = iterations+1
        print(str(float(iterations)/(len(file_list)-1)*100)+"%\n")
