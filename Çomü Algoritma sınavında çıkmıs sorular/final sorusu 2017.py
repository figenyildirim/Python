#2017 final sorusu: özet olarak hangi sayının onlar basamagının birler basamagındaki rakam kadar kuvveti ile binler basamagının yuzler basamagındaki rakam kadar kuvvetinin carpımı syıya eşit ise yazdır.
saniye=1000
dizi=[]
d=1
while d==1:
    a=1
    sayi=saniye
    while a!=0:
        a=sayi//10
        deger=sayi%10
        dizi.append(deger)
        sayi=a
    if (dizi[1]**dizi[0])*(dizi[3]**dizi[2])==saniye:
        print(saniye)
        break
    else:
        dizi.clear()
        saniye=saniye+1
