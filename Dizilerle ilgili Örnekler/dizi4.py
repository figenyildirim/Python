#diziyi kontrol edip asal sayiları baska diziye atayan kod
dizi=[4,9,7,13,85,96,91,88,44,5,19,2]
asaldizi=[]
n=len(dizi)
d=1
i=0
while i!=n:
    z=2
    while d==1:
        if dizi[i]==2:
            asaldizi.append(dizi[i])
            i=i+1
            break
        if dizi[i]%z==0:
            i=i+1
            break
        else:
            if z>dizi[i]**(1/2):
                asaldizi.append(dizi[i])
                i=i+1
                break
            else:
                z=z+1

print(asaldizi)
    
