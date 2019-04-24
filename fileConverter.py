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
        print(file)
        file=open(file,"w+")
        file.write(str(languageNum)+",")
        for i in range (0,mfcc_counts-1):
            file.write(str(fileContent[i][0])+",")
        file.write(str(fileContent[mfcc_counts-1][0]))
        file.close()
        iterations = iterations+1
        print(str(float(iterations)/(len(file_list)-1)*100)+"%\n")
