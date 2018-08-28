# LOGIC: IF, ELSE IF & ELSE
# ...........soal 1.............

# x=input('Masukan Angka : ')
# if ((int(x)%2)==1) :
#     print('angka '+ x + ' GANJIL')
# else :
#     print('angka '+ x + ' GENAP')


# ...........soal 2.............
# Massa=float(input('Masukan massa (kg) :'))
# Tinggi=float(input('Masukan tinggi (cm) :'))
# print('Massa ' + str(Massa) + ' Kg ' + ' Tinggi ' + str(Tinggi/100) + ' m')
# IMT=Massa/pow(Tinggi/100,2)
# if (IMT>39.9) :
#     print('IMT = '+ str(IMT) + ', Obesitas!!!')
# elif (IMT>=30.0) :
#     print('IMT = '+ str(IMT) + ', Berat Badan Sangat Berlebih!!!')
# elif (IMT>=25.0) :
#     print('IMT = '+ str(IMT) + ', Berat Badan Berlebih!!!')
# elif (IMT>=18.5) :
#     print('IMT = '+ str(IMT) + ', Berat Badan Ideal')
# else :
#     print('IMT ='+ str(IMT) +', Berat Badan Kurang')

# lebih efisien jika printnya ditaruh di bawah sendiri



# for urut in range(0,21,2):
#     print('no urut ' + str(urut))

# z='';
# i=1
# for y in range(5):
#     for x in range(y+1):
#         z += " * ";
        
#     # i += 1
#     z += "\n"

# print(z)

# ...........soal 1.............
# z='';
# n=5
# i=n
# for y in range(n):
#     for x in range(i):
#         z += " * ";
        
#     i -= 1
#     z += "\n"

# print(z)

#baron ways
# size= int (input("Masukan size"))
# z=''
# for num in range (size):
#     for num1 in range (num,size):
#         z += ' * '
#     z += '\n'
# print(z)

# ...........soal 2.............
# z='';
# i=int(input('masukan lebar :'))
# n=2*i-1
# for y in range(n):
#     if (y<n/2) :
#         for x in range(i):
#             z += " * ";
#         i -= 1
#         z += "\n"
#     else :
#         i +=1
#         for x in range(i+1):
#             z += " * ";
#         z += "\n"
# print(z)

#baron ways 
# size= int (input("Masukan size : "))
# z=''
# for num in range (size):
#     for num1 in range (num,size):
#         z += ' * '
#     z += '\n'
# for num in range (size-1):
#     for num1 in range (0, num+2):
#         z += ' * '
#     z += '\n'

# print(z)

# ...........soal 3.............
# z=''
# y=int(input('masukan tinggi segitiga :'))

# k=y-1
# for tinggi in range (y):
#     for lebar in range (k):
#         z += '   '
#     for bintang in range((2*(y-k))-1):
#         z += ' * '
#     k -= 1
#     z += '\n'
# print (z)

# Baron Ways
# size = int(input('Masukan size: '))
# z =""
# for num in range (size):
#     for num1 in range (0, size-1-num):
#         z += '   '
#     for num2 in range (0, (num*2)+1):
#         z += ' * '
#     z += '\n'
# print(z)

# ...........soal 4............
# z = ''
# y=int(input('masukan tinggi segitiga :'))
# k=0
# for tinggi in range (y):
#     for lebar in range (k):
#         z += '   '
#     for bintang in range ((2*(y-k))-1):
#         z += ' * '
#     k += 1
#     z += '\n'
# print(z)

# Baron Ways
size = int(input('Masukan size: '))
z =""

for num in range(size):
    for num1 in range(0, num):
        z += "   "
    for num2 in range (0,(size*2)-(num*2)-1):
        z += ' * '
    z += '\n'
print(z)

# ...........soal 5............

# z = ''
# y=int(input('masukan tinggi segitiga :'))
# n=1+int(y/2)
# k=n
# for tinggi in range (y):
#     if (tinggi < n):
#         k -= 1
#         for lebar in range (k):
#             z += '   '
#         for bintang in range ((2*(n-k))-1):
#             z += ' * '
#         z += '\n'
#     else :
#         k += 1
#         for lebar in range(k):
#             z += '   '
#         for bintang in range (2*(n-k)-1):
#             z += ' * '
#         z += '\n'        
# print(z)

# BARON WAYS
# jawaban no 3 dilanjutkan dengan cara no 4 dengan size di no 3 range nya (1,size) 


# ...........soal 6............
# z = ''
# y=int(input('masukan lebar :'))
# n=1+int(y/2)
# k=2
# for tinggi in range (y):
#     if (tinggi == 0 or tinggi == (y-1)):
#         for bintang in range (y):
#             z += ' * '
#         z += '\n'
#     else:
#         if (tinggi<=(y/2)):
#             for kiri in range (n-tinggi):
#                 z += ' * '
#             for kosong in range ((2*tinggi)-1):
#                 z += '   '
#             for kanan in range (n-tinggi):
#                 z += ' * '
#         else:
#             for kiri in range (k):
#                 z += ' * '
#             for kosong in range ((2*(n-k))-1):
#                 z += '   '
#             for kanan in range (k):
#                 z += ' * '
#             k += 1
#         z += '\n'
        
# print(z)

# BARON WAYS
# size = int(input('Masukan size: '))
# z =""

