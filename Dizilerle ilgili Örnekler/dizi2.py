#diziyi kucukten buyuge sıralama
n=int(input("diziniz kac elemanli olsun:"))
dizi=[]
for i in range(0,n):
    eleman=int(input("lutfen bir eleman girin:"))
    dizi.append(eleman)
    #dizi.sort(reverse=True) bunu eklersem buyukten kucuge sıralar
print(dizi)
