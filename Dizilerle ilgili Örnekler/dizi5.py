#dizinin en buyuk elemanın basamk degrleri toplamını bulan kod
dizi=[9,78,956,84515,236548,796135,157,545,458914]
dizi.sort(reverse=True)
sayi=dizi[0]
a=1
toplam=0
while a!=0:
    a=sayi//10
    deger=sayi%10
    toplam=toplam+deger
    sayi=a
print(dizi)
print(toplam)
    
