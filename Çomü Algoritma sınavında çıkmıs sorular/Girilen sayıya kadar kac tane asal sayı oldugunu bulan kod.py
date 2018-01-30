#Girilen sayıya kadar kac tane asal sayı oldugunu bulan kod
n=int(input("lutfenbir sayi girin: "))
sayac=0
i=2
sayi=1
while sayi!=n:
    if sayi%i==0:
        sayi=sayi+1
        i=2
    else:
        if i>sayi**(1/2):
            sayac=sayac+1
            sayi=sayi+1
            i=2
        else:
            i=i+1
print(sayac)
    
    
