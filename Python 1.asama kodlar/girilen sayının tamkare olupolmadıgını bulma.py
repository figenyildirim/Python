#Girilen sayının tamkare olup olmadıgını bulma
sayi=input("bir sayi gir: ")
kontrol=int(sayi)**(1/2)
if int(sayi)==kontrol*kontrol:
    print ("girilen sayi tam karedir.")
else:
    print ("girilen sayi tam kare degildir.")
