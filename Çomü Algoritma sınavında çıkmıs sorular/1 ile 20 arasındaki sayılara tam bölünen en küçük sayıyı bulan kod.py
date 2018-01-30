#1 ile 20 arasındaki sayılara tam bölünen en küçük sayıyı bulan kod
i=1
sayi=1
while i<21:
    if sayi%i==0:
        i=i+1
    else:
        sayi=sayi+1
        i=1
print(sayi)
    
        
