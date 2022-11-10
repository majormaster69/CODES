import sys
import random
n = int(input("ENter the no.of objects"))
obj = input("\nEnter objects spereated by commas:")
print("\nList of OBJ",obj)
k = int(input("\nEnter no of clusters:"))
print("\nAssumed k=",k)
dataSet=obj.split(',')
myDict1={}
myDict2={}
try:
    means = random.sample(dataSet,k)
except ValueError:
    print("\nOOPS ")
    sys.exit()
if k==1:
    print(dataSet)
elif k==len(dataSet):
    print(dataSet)
else:
    i=0
    while(i<k):
        myDict1[i]=[]
        myDict2[i]=[]
        i=i+1
    c=0
    while True and c<50:
        c = c+1
        minDist = sys.maxsize
        kNumber = -1
        for i in dataSet:
            minindex = 9
            minValue = sys.maxsize
            key = 0
            while(key<len(means)):
                if abs(int(means[key]) - int(i)) < minValue:
                           minindex = key
                           minValue = abs(int(means[key]) - int(i))
                key = key +1
            myDict1[minindex].append(i)
        if(myDict1 == myDict2):
                           break
        for key in myDict1:
            sumOfk =0
            myDict2[key] = []
            for j in myDict1[key]:
                sumOfk = sumOfk + int(j)
                myDict2[key].append(j)
            means[key] = sumOfk / len(myDict1[key])
            myDict1[key] = []
print("Required Clusters are:\n")
print(myDict2)
























                           
