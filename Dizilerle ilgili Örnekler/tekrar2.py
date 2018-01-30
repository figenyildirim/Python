#girilen sayinin basamaak degerlerini bir diziye atama
sayi=int(input("lutfen bir sayi girin: "))
dizi=[]
a=1
deger=0
while a!=0:
    a=sayi//10
    deger=sayi%10
    dizi.append(deger)
    sayi=a
dizi.reverse()
print (dizi)
