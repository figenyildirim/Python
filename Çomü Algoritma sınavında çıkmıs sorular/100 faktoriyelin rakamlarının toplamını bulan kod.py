#100! rakamlarının toplamını bulan kod
faktoriyel=1
toplam=0
a=1
for i in range(1,101):
    faktoriyel=faktoriyel*i
while a!=0:
    a=faktoriyel//10
    deger=faktoriyel%10
    toplam=toplam+deger
    faktoriyel=a
print(toplam)
