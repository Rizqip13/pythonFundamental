print (" _    _\n|_|    |\n|_|    |")
def menu1():
    while(True):
        temp=int(input("\n\nMasukan angka: "))
        if(temp>=0 and temp<=9):
            ikilist.append(temp)
            break
        else:
            print("tidak dapat menerima angka negatif atau lebih dari 1 digit")

def sevenseg(listini):
    digit=len(listini)
    hasil=""
    #baris 1 ngisi a untuk setiap digit
    for a in listini:
        if (a==1 or a==4):
            hasil+= "     "
        else:
            hasil+= " _   "
    hasil+="\n"
    #baris 2 ngisi f g b untuk setiap digit
    for fgb in listini:
        #f nya
        if (fgb==1 or fgb==2 or fgb == 3 or fgb == 7):
            hasil+=" "
        else:
            hasil+="|"
        #g nya
        if (fgb==0 or fgb==1 or fgb == 7):
            hasil+=" "
        else:
            hasil+="_"
        #b nya
        if (fgb==5 or fgb==6):
            hasil+="   "
        else:
            hasil+="|  "
    hasil+="\n"
    #baris 3 ngisi e d c
    for edc in listini:
        #e nya
        if (edc==0 or edc==2 or edc == 6 or edc == 8):
            hasil+="|"
        else:
            hasil+=" "
        #d nya
        if (edc==1 or edc==4 or edc == 7):
            hasil+=" "
        else:
            hasil+="_"
        #c nya
        if (edc==2):
            hasil+="   "
        else:
            hasil+="|  "
    return hasil



ikilist=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sevenseg(ikilist))
ikilist=[]
while (True):
    P=int(input("Selamat Datang di SevenHoki\n\nMain Menu:\n  1. Isi List\n  2. Lihat List\n  3. Keluar\nMasukan Pilihan : "))
    if (P==1):
        menu1()
    elif (P==2):
        print(sevenseg(ikilist))
        ikilist=[]
    elif (P==3):
        break
    else:
        print('\n\n\n Tolong Masukan input sesuai dengan pilihan cuk\n\n\n')