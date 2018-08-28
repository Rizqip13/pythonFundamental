# INTRO TO PYTHON
# ...........soal 1.............

# x=4
# y=3
# z=2
# w=((x+y*z)/(x*y))**z
# print(w)


# ...........soal 2.............

# a= input('masukan angka berapapun :')
# print('kuadrat dari ' + a + ' = ' + str(pow(int(a),2)))


# ...........soal 3.............

# import math
# totalhari=485
# tahun=math.floor(totalhari/360)
# bulan=math.floor((totalhari%360)/30)
# minggu=math.floor(((totalhari%360)%30)/7)
# hari=math.floor(((totalhari%360)%30)%7)
# print(str(totalhari) + ' hari adalah ' + str(tahun) +' tahun ' + str(bulan) + ' bulan ' + str(minggu) + ' minggu ' + str(hari) +' hari')


# ...........soal 4.............

# totalumur=49 #andi + Budi
# rasio=0.4 #andi terhadap budi
# umBudi=totalumur/(rasio+1)
# umAndi=totalumur-umBudi
# print('umur Budi 2 tahun lagi: ', str(umBudi+2))
# print('umur Andi 2 tahun lagi: ', str(umAndi+2))


# ...........soal 5.............

# x = 'Halo Dunia';
# print(x.count('a'));


# ...........soal 6.............

import math
Jarak=120 #km
vA=60 #km/jam dari timur
vB=40 #km/jam dari barat
waktuAwal=9 #jam 9
T=Jarak/(vA+vB) #dalam jam  
jam=math.floor(T) 
menit=(T-jam)*60 
print('Terjadi tabrakan pada pukul '+str(waktuAwal+jam)+':'+str(round(menit)))

#bisa juga dibawa ke detik dulu
T=Jarak*3600/(vA+vB)
jam=math.floor(T/3600)
menit=math.floor((T%3600)/60)
detik=math.floor((T%3600)%60)
print('Terjadi tabrakan pada setelah '+str(jam)+' jam '+str(menit)+ ' menit ' + str(detik) + ' detik');
