# x=[40,100,1,5,25,10]
# print(x)
# x.sort()
# print(x)
# x.sort(reverse=True)
# print(x)

# Contoh recrusive function
# def pangkat(x,y):
#     if(y==1):
#         return x
#     else:
#         y-=1;
#         return x * pangkat(x,y)

# print(pangkat(3,2))

# def kali(angka1 = 5, angka2 = 2) :
#     return angka1 * angka2;
# print(kali(angka2=4));
# print(kali(2,3))

# mobil= ['ayla', 'xenia', 'avanza']

# print(mobil[1:3])

# def sortAsc(x):
#     #bikin
#     for iterasi in range(1,len(x)):
#         for i in range (len(x)-iterasi):
#             if (x[i]<x[i+1]):
#                 x[i],x[i+1]=x[i+1],x[i]
#                 print(x)
#     return x

# def sortDesc(x):
#     for iterasi in range(1,len(x)):
#         for i in range (len(x)-iterasi):
#             if (x[i]<x[i+1]):
#                 x[i],x[i+1]=x[i+1],x[i]
#     return x

def ngurut(x,reverse=0): #untuk desc ubah nilai reverse jadi 1
    for iterasi in range(1,len(x)):
        for i in range (len(x)-iterasi):
            if (x[i+reverse]>x[i+1-reverse]):
                x[i],x[i+1]=x[i+1],x[i]
                print(x)
    return x

#BARON WAYS
def urut(thelist, kucingbertasbih):
    for i in range (len(thelist)):
        for j in range (i+1, len(thelist)):
            check = kucingbertasbih(thelist[i],thelist[j]) #kucingbertasbih jika b-a maka desc kalau a-b maka asc
            if (check >0):
                thelist[i],thelist[j]=thelist[j],thelist[i]
    return thelist

y=[40,100,1,5,25,10]
print(urut(y,lambda a,b : b-a)) #b-a maka desc
print(urut(y,lambda a,b : a-b)) #a-b maka asc

def Cari(x):
    kecil=x[0]
    besar=x[0]
    for i in range (len(x)):
        if (x[i]<kecil):
            kecil=x[i]
        elif (x[i]>besar):
            besar=x[i]
    print(f"Nilai terkecil adalah {kecil}")
    print(f"Nilai terbesar adalah {besar}")
    return [kecil,besar]

# x=[50, 120, -1, 5, 25, 50]
# y=[40,100,1,5,25,10]
# z=[1,2,3,7,4,10]

# print(f"{y} \n-----------------------")
# # Cari(y)

# # print(sortDesc(y))
# print(ngurut(y,1))
# # print(sortAsc(z))
# # print(ngurut(y))

# # print(x)
# # Cari(x)

# # print(sortDesc(x))
# # print(sortAsc(x))

# for i in range (0):
#     print(i)