#negatif ve pozitif elemanların sayisini veren kod
dizi=[2,-4,9,8,-7,-6,-45,0,78,96,-852,-64,963,0]
p=0
n=0
uzunluk=len(dizi)
for i in range(0,uzunluk):
    if dizi[i]>0:
        p=p+1
    if dizi[i]<0:
        n=n+1
print("pozitif elemanlar=",p)
print("negatif elemanlar=",n)
print(uzunluk)
sifir=uzunluk-(p+n)
print("sifirlarin sayisi=", sifir)

       
