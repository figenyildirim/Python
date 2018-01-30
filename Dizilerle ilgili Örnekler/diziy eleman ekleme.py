sayac=0
liste = []
sayi = int(input("kaç tane sayı değeri gireceksiniz"))
while (sayac<sayi):
    a = float(input("bir sayı giriniz"))
    liste.append(a)#listeye tekrar ekle
    sayac+=1
i=0#dizinin elemanlarını en baştan tekrar yazmak için sıfırladık
while i<sayi:
    print(liste[i])#dizinin i indisindeki değerindeki elemanını yaz
    i+=1
