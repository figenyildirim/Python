#rastgele bir eleman üret ve bu dizide varsa var yoksa yok yazsın
import random
sayi=random.randint(1,100)
dizi=[99,75,84,62,1,2,22,54,96,46,35,81,26,76,82,15,16,18,19,52,63]
n=len(dizi)
i=0
d=1
while i!=n:
    if dizi[i]==sayi:
        print(sayi, "dizi de vardır")
        d=2
        break
    else:
        i=i+1
if d==1:
    print(sayi, "dizide yoktur")
      
