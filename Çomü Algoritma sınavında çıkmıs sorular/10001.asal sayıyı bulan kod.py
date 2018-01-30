#10001.asal sayıyı bulan kod
sayi=3
sayac=1
i=2
d=1
while d==1:
    if sayi%i==0:
        sayi=sayi+1
        i=2
    else:
        if i>sayi**(1/2):
            sayac=sayac+1
            if sayac==10001:
                print(sayi)
                break
            else:
                sayi=sayi+1
                i=2
        else:
            i=i+1
