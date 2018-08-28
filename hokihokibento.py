Nama=['Paket Hoki A', 'Paket Hoki B', 'Paket Hoki C']
Harga=[20000,25000,30000]
Beli=[]
total=0
kembalian=0
while (True):
    print('------------HOKI HOKI BENTO------------')
    print('---Selamat Datang Selamat Berbelanja--- ')
    print('Main Menu: \n  1. Lihat Menu\n  2. Lihat Chart\n  3. Checkout\n  4. Keluar')
    c=int(input('Masukan Pilihan:'))
    if (c==1):
        while(True):
            for items in range (len(Nama)):
                print (f'{items+1}. {Nama[items]} Rp {Harga[items]}')
            print("\nMasukan '0' Untuk kembali ke menu utama")
            a=int(input('Pilih Paket :'))
            if (a==0):
                break
            elif (a>0 and a<len(Nama)) :
                Beli.append(a-1)
    elif(c==2):
        for items in range(len(Beli)):
            print(f'{items+1}. {Nama[Beli[items]]} Rp {Harga[Beli[items]]}')
            total += Harga[Beli[items]]
        print('--------------------------')
        print(f'Total Harga   = Rp {total} \n \n')
    elif(c==3):
        while(True):
            total=0
            for items in range(len(Beli)):
                print(f'{items+1}. {Nama[Beli[items]]} Rp {Harga[Beli[items]]}')
                total += Harga[Beli[items]]
            print('--------------------------')
            print(f'Total Harga   = Rp {total}')
            uang=int(input('Masukan Uang :  Rp '))
            if (uang<total):
                print('\n\nUang Anda Kurang!\n\n ')
            else:
                kembalian=uang-total
                print(f'Terimakasih, Kembalian uang anda Rp {kembalian}')
                total=0
                kembalian=0
                Beli=[]
                break
    elif(c==4):
        break