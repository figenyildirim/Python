# 1 ile 100 arasında sayı üretiyoruz 42 olunca kacıncı seferde buldugunu ekrana yazıp programdan cıksın
import random
d=1
i=1
while d==1:
    sayi=random.randint(1,100)
    if sayi==42:
        print(i)
        break
    else:
        i=i+1
