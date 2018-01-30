#negatif ve pozitifelemanalrı ayrı ayrı dizilere atayan kod
dizi=[1,4,-7,12,5,-9,-6,45,63,18]
dizi1=[]
dizi2=[]
for i in range(0,9):
    if dizi[i]<0:
        dizi1.append(dizi[i])
        i=i+1
    else :
        dizi2.append(dizi[i])
        i=i+1
print("negatif dizi:", dizi1)
print("pozitif dizi", dizi2)
                     
    
    
