#kulanıcıdan bir sayı oku asal olup olmadıgını yazan kod
sayi=int(input("bir sayi girin: "))
a=1
i=2
while a==1:
    if sayi%i==0:
        print("sayi asal degildir.")
        break
    else:
        if i>sayi**(1/2):
            print("sayi asaldır.")
            break
        else:
            i=i+1
