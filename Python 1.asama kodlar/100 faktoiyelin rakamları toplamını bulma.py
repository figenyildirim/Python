#100! rakamları toplamını bulan kod
sonuc=1
a=1
b=0
toplam=0
for i in range(1,100):
    sonuc=sonuc*i
n=sonuc
while a!=0:
    a=sonuc//10
    b=sonuc%10
    toplam+=b
    sonuc=a
print (n )
print (toplam)
