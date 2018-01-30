#n elemanli bir dizide 3 ile tam bölünen sayiların baska bir diziye yüklenmesini sağlayan kod
dizi1=[]
dizi2=[]
sinir=int(input("dizinin kac elemanli olmasni istesiniz:"))
for i in range(0,int(sinir)):
    eleman=int(input("lutfen bir eleman girin:"))
    dizi1.append(eleman)
    if eleman%3==0:
        dizi2.append(eleman)
print ("ilk dizi",dizi1)
print ("3 ile tam bolune sayilarin toplandigi dizi",dizi2)
