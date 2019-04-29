import glob,numpy
mfcc_counts=13
file_list = glob.glob("./*.csv")
iterations=0
for file in file_list:
        language = file[2:][:2]
        if language=="de":
            languageNum=1
        if language=="en":
            languageNum=2
        if language=="es":
            languageNum=3
        fileContent=numpy.genfromtxt(file,delimiter=',')
        file=open(file,"w+")
        file.write(str(languageNum))
        for i in range (0,len(fileContent)):
            for j in range(0,20,5):
                file.write(","+str(fileContent[i][j]))
        file.close()
        iterations = iterations+1
        print(str(float(iterations)/(len(file_list))*100)+"%\n")
