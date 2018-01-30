#1 den girilen sayıya kadar olan sayıların toplamının karesi ile karesiin toplamı arasındaki farkı bulan kod
n=int(input("lutfen bir sayi girin:"))
karetoplam=0
toplam=0
fark=0
for i in range(1,(n+1)):
    toplam=toplam+i
    karetoplam=karetoplam+(i**2)
fark=(toplam**2)-karetoplam
print(fark)
    
