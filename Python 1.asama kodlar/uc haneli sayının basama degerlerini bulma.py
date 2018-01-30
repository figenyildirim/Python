#3 basamaklı bir sayıyı basamak degerlerine ayırma
sayi=input("lutfen bir sayi girin")
a=int(sayi)%100
yb=(int(sayi)-a)/100
b=a%10
ob=(a-b)/10
print("yuzlerbasamagı",yb , "onlarbasamagı" ,ob, "birlerbasamagı", b)
