#10 elemananlibir sayi dizisinde neg ve poz sayifaların ayrı ayrı ortalamalarını bulan
dizi=[]
neg=0
poz=0
for i in range(0,10):
    eleman= int(input("lutfen bir sayi girin:"))
    dizi.append(eleman)
    if eleman<0:
        neg=neg+eleman
    else:
        poz=poz+eleman
print ("negatif elemanlarin ortalamasi",neg/10)
print ("pozitif elemanlarin ortalamasi",poz/10)
