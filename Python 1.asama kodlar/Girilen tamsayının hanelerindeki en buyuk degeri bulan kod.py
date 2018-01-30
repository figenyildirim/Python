#girilen sayının hanelerindeki en büyük rakamı bulma
sayi=input("bir sayı girin")
eb=0
while sayi!=0:
     b=(int(sayi)%10)
     sayi=int(sayi)//10
     if eb<b:
         eb=b
print (eb)
