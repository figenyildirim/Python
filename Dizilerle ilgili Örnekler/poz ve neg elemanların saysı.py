#istenilfigi ladar elemandan oluşan bir dizide neg vepozitiflerin sayısını bulan kod
sayac=0
dizi=[]
neg=0
poz=0
sinir=int(input("kac elemanli bir dizi olusturmak istiyorsunuz:"))
while sayac<sinir:
    eleman=int(input("lutfen bir eleman girin:"))
    dizi.append(eleman)
    if eleman==0:
        continue
    if eleman<0:
        neg=neg+1
    else:
        poz=poz+1
    sayac=sayac+1
print ("negatif elemanalrin sayisi:",neg)
print ("negatif elemanalrin sayisi:",poz)
