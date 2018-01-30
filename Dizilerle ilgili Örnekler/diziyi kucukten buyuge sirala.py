sinir=int(input("diziniz kac elemandan olussun:"))
dizi=[]
for i in range(0,int(sinir)):
    eleman=int(input("lutfen bir eleman girin:"))
    dizi.append(eleman)
    dizi.sort()
print (dizi)
