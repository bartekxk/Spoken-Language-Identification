import glob,numpy,math

class simplePriorityQueue:
        def __init__(self,size):
                self.list=[]
                self.size=size
                for i in range(0, size):
                        self.list.append([0.0,999999.0])
        def add(self,value,langugae):
                if value==0.0:
                        return
                place=-1
                for i in range(0,self.size):
                        if value>=self.list[i][1]:
                                break
                        place=place+1
                for i in range(0,place):
                        self.list[i]=self.list[i+1]
                if place != -1:
                        self.list[place]=[langugae,value]
        def printValues(self):
                for i in range(0,self.size):
                        print(self.list[i])
        def getLanguage(self):
                languages=[0,0,0,0]
                for i in range(0,self.size):
                        languages[int(self.list[i][0])]=languages[int(self.list[i][0])]+1
                if languages[1]==languages[2] and languages[2]==languages[3]:
                        return self.list[self.size-1][0]
                max=languages[1]
                maxLanguage=1
                for i in range(1,4):
                        if(languages[i]>max):
                                max=languages[i]
                                maxLanguage=i
                strLanguage="de"
                if maxLanguage==2:
                        strLanguage="en"
                if maxLanguage==3:
                        strLanguage="es"
                return maxLanguage
        def resetValues(self):
                self.list = []
                for i in range(0, self.size):
                        self.list.append([0.0,999999.0])
mfcc_counts=52
def calculate(a,b):
        sum=0
        for i in range(1,mfcc_counts):
                sum+=(a[i]-b[i])*(a[i]-b[i])
        return math.sqrt(sum)


queue15=simplePriorityQueue(15)
queue10=simplePriorityQueue(10)
queue5=simplePriorityQueue(5)
queue1=simplePriorityQueue(1)
file_list = glob.glob("./*.csv")
data_set=[]
print("Loading data set...\n")
for i in range(0,len(file_list)):
        data_set.append(numpy.genfromtxt(file_list[i],delimiter=',').tolist())

print("Done!\nWorking...\n")
attemps=0
success1=0
success5=0
success10=0
success15=0
test_list=glob.glob("/home/bartek/si/13x13/MFCCtest/*.csv")
for test_file in test_list:
        test_set=numpy.genfromtxt(test_file,delimiter=',')
        for x in data_set:
                result=calculate(x,test_set)
                queue15.add(result, x[0])
                queue10.add(result,x[0])
                queue5.add(result, x[0])
                queue1.add(result, x[0])
        attemps = attemps + 1
        #print queue.getLanguage(), test_set[0]
        if queue10.getLanguage() == test_set[0]:
                success10 = success10 +1
        if queue5.getLanguage() == test_set[0]:
                success5 = success5 +1
        if queue1.getLanguage() == test_set[0]:
                success1 = success1 +1
        if queue15.getLanguage() == test_set[0]:
                success15 = success15 + 1
        queue1.printValues()
        print(queue1.getLanguage())
        queue15.resetValues()
        queue10.resetValues()
        queue5.resetValues()
        queue1.resetValues()
        print(str(float(attemps)/len(test_list)*100)+"%\n")
print(str(float(success1)/attemps*100)+"% efficiency for 1 nh\n")
print(str(float(success5)/attemps*100)+"% efficiency for 5 nh\n")
print(str(float(success10)/attemps*100)+"% efficiency for 10 nh\n")
print(str(float(success15)/attemps*100)+"% efficiency for 15 nh\n")

print("Done!\n")
