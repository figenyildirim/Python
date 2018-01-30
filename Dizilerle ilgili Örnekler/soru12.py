#istenilen deger girilene kadra diziye eleman ekleniyor
#istenilen ddegr girildiginde aritmatik ortalama hesaplanıyor
print ("eleman olarak -1 girerseniz program durur.")
dizi=[]
eleman=0
i=0
toplam=0
while eleman!=-1:
    eleman=int(input("lutfen bir eleman girin:"))
    if eleman==-1:
        break
    i=i+1
    dizi.append(eleman)
    toplam=toplam+eleman
print (toplam/i)


    
    
    
