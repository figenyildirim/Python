#2^1000 rakamları toplamını bulan kod
sayi=2**1000
toplam=0
a=1
while a!=0:
    a=sayi//10
    deger=sayi%10
    toplam=toplam+deger
    sayi=a
print(toplam)
    
