#bir dizi olusturup ekrana basma
dizi=[]
sayac=0
sayi=int(input("kac elemanlı bir dizi olusturmak istersiniz:"))
while (sayac<sayi):
         eleman=int(input("diziye eklemek istediginiz sayiyi girin:"))
         dizi.append(eleman)
         sayac+=1
print (dizi)
