#sayi tahmin etme oyunu
import random
rastgelesayi=random.randint(1,100)
for i in range(1,10):
    tahmin=input("lutfen bir tahminde bulunun:")
    if int(rastgelesayi)==int(tahmin):
        print ("bravoo dogru tahmin!")
        break
    if int(rastgelesayi)<int(tahmin):
        print ("ipucu!!! daha kucuk bir tahminde bulununuz.")
    else:
        print ("ipucu!!! daha buyuk bir tahminde bulununuz.")
               
                            
