import numpy
# y=range(16)
# y=reshape(y,(4,4))

# def kiri(x):
#     # num=int(input("Berapa kali? "))
#     # for i in range  :
#     x[0][0],x[0][1],x[0][2],x[0][3],x[1][3],x[2][3],x[3][3],x[3][2],x[3][1],x[3][0],x[2][0],x[1][0]=x[0][3],x[1][3],x[2][3],x[3][3],x[3][2],x[3][1],x[3][0],x[2][0],x[1][0],x[0][0],x[0][1],x[0][2]
#     print(x)

# def kanan(x):
#     # num=int(input("Berapa kali? "))
#     # for i in range num :
#     x[0][3],x[1][3],x[2][3],x[3][3],x[3][2],x[3][1],x[3][0],x[2][0],x[1][0],x[0][0],x[0][1],x[0][2]=x[0][0],x[0][1],x[0][2],x[0][3],x[1][3],x[2][3],x[3][3],x[3][2],x[3][1],x[3][0],x[2][0],x[1][0]
#     print(x)

# print(y)

# while True:
#     pilih=int(input('1. Putar Kanan\n 2. Putar Kiri\n 3. Keluar\n Masukan Pilihan : '))
#     if pilih == 1:
#         kanan(y)
#     elif pilih == 2:
#         kiri(y)
#     elif pilih == 3:
#         break
#     else:
#         print("masukan sesuai pilihan yang ada")

# x=numpy.zeros((3,3,3))
# k=0
# for i in range (3):
#     for j in range(3):
#         for l in range (3):
#             x[i][j][l]=k
#             k+=1
# print(x)

def cetakmat(x):
    for i in range (len(x)):
        print(x[i])

list1=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
hasil=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# hasil[0][0]=list1[3][0]
# hasil[0][1]=list1[2][0]
# hasil[0][2]=list1[1][0]
# hasil[0][3]=list1[0][0]
for i in range (4):
    for index1, index2 in zip(range (4),range (3,-1,-1)):  #zip agar bisa 2 variable
        hasil[i][index1]=list1[index2][i]

cetakmat(list1)
print("\n")
cetakmat(hasil)
    



