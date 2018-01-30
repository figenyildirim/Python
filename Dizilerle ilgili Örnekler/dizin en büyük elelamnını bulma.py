#10 elemanli bir dizinin en büyük elemanini bulan kod
dizi=[]
for i in range(0,10):
    eleman=int(input("lutfen diziye bir eleman girin:"))
    dizi.append(eleman)
    dizi.sort()
print (dizi[9])
    
    
