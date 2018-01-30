#bir sayı kadar noktadan üçgen oluşturabiliyorsak o syıya üçgen sayı denir.
# örneğin 1,3 ve 6 üçgen sayılardır
# .     .     .
#      . .   . .
#           . . .
#girilen sayının üçgen sayı olup olmadıgını bulan kod
sayi=int(input("lutfen bir sayi girin:"))
toplam=0
for i in range(1,sayi+1):
    toplam=toplam+i
    if toplam>sayi:
        print("ucgen sayi degildir.")
        break
    if toplam==sayi:
        print("ucgen sayidir.")
        break
    
    
