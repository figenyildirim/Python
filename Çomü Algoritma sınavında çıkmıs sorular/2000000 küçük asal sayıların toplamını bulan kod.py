#2000000 küçük asal sayıların toplamını bulan kod
sayi=3
toplam=2
i=2
while sayi<2000000:
    if sayi%i==0:
        sayi=sayi+1
        i=2
    else:
        if i>sayi**(1/2):
            toplam=toplam+sayi
            sayi=sayi+1
            i=2
        else:
            i=i+1
print(toplam,sayi)
