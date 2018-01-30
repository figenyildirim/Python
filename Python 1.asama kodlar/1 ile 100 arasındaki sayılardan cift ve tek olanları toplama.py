#1 ile 100 arasındaki sayılardan çift ve tek olanların ayrı ayrı toplamlarını bulma
cifttoplam=0
tektoplam=0
for sayi in range(0,100):
    if int(sayi)%2==0:
        cifttoplam=cifttoplam+sayi
    else:
        tektoplam=tektoplam+sayi
print (cifttoplam,tektoplam) 
