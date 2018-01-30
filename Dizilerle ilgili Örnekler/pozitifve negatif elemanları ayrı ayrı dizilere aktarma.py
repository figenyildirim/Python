#negatif ve pozitif elemanlari ayri ayri dizilere yazma
dizi1=[]
dizi2=[]
for i in range(0,10):
    eleman=int(input("lutfen bir eleman girin:"))
    if eleman==0:
        continue
    if eleman<0:
        dizi1.append(eleman)
    else:
        dizi2.append(eleman)
print ("pozitif elemanlar dizisi", dizi2)
print ("negatif elemanlar dizisi", dizi1)

        
