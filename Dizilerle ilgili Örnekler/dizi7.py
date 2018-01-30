#dizideki elemanlarının carpımlarının basmak degerlerinin toplamını bulan kod
dizi=[4,8,9,7,5,6]
n=len(dizi)
carpim=1
toplam=0
a=1
for i in range(0,n):
    carpim=dizi[i]*carpim
c=carpim
while a!=0:
    a=c//10
    deger=c%10
    toplam+=deger
    c=a
print(carpim,toplam)
    
