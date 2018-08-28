def FizzBuzz(x):
    for num in range (1,x+1):
        if (num%3==0 and num%5==0):
            print('FizzBuzz')
        elif (num%5==0):
            print('Buzz')
        elif (num%3==0):
            print('Fizz')
        else:
            print(num)

def Fibo(num):
    listFibo=[1,1]
    for i in range (1,num-1):
        # listFibo += [listFibo[i]+listFibo[i-1]]
        listFibo.append(listFibo[i]+listFibo[i-1])
    print(listFibo[num-1])
    print(listFibo)

def reverseList(iniList):
    # print(iniList)
    for i in range(int(len(iniList)/2)):
        iniList[i],iniList[-(i+1)]=iniList[-(i+1)],iniList[i]
    print(iniList)

import math
def mean(iniList):
    return (round(sum(iniList)/len(iniList)))

def median(iniList):
    iniList.sort()
    if (len(iniList)%2==0):
        hasil=mean([iniList[math.floor(len(iniList)/2)],iniList[math.floor(len(iniList)/2)-1]])
    else :
        hasil=iniList[int(len(iniList)/2)]
    return hasil

def modus(adaList):
    s=list(set(adaList))
    angkajumlah=[]
    for num in s:
        angkajumlah.append(adaList.count(num))
    #menentukan ada modus atau tidak
    x=max(angkajumlah)
    hasil=[]
    for num in range (len(angkajumlah)):
        if(angkajumlah[num]==x):
            hasil.append(s[num])
    if (len(s)==len(hasil)):
        hasil=[] #tidak ada modus
    return hasil



# FizzBuzz(20)
# Fibo(6)
# reverseList([1,2,3,4,5,6,7,8])


inidata = [ 1, 2, 3, 2, 5, 2, 2, 7, 2]
data2=[2,3,2,3,1,1,5]
# print(inidata.count(2))
print(f"modusnya adalah {modus(data2)}")
# print(s)
