#10 sayıdan kacının pozitif kacının negatif oldugunu bulma
nsayac=0
psayac=0
gereksiz=0
for i in range(1,11):
    sayi=input("lutfen birsayi girin : ")
    if int(sayi)<0:
        nsayac=nsayac+1
    else:
        psayac=psayac+1
print (nsayac, "tane negatif sayi vardir")
print (psayac, "tane pozitif sayi vardir")
