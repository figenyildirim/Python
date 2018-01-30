#10 elemanlı bir dizinin negatif elemanlarının toplamını bulma
dizi=[]
toplam=0
for i in range(0,10):
    eleman=int(input("lutfen bir eleman girin:"))
    dizi.append(eleman)
    if eleman<0:
        toplam=toplam+eleman
print (dizi)
print ("dizideki negatif elelmanların toplamı", toplam)
