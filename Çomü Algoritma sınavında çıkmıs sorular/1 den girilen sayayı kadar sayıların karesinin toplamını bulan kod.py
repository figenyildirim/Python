#1'den girilen sayayı kadar sayıların karesinin toplamını bulan kod
n=int(input("lutfen bir sayi girin:"))
toplam=0
for i in range(1,n+1):
    toplam=toplam+(i**2)
print(toplam)
