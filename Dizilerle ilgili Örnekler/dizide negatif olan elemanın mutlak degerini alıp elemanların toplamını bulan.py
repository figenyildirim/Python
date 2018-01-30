dizi=[]
toplam=0
for i in range(0,10):
    eleman=int(input("lutfen bir sayi girin"))
    dizi.append(eleman)
    if eleman<0:
        eleman=((-1)*eleman)
        toplam=toplam+eleman
    else:
        toplam=toplam+eleman
print (toplam)
    
