#size gelen mektuplardan mektubun baslıgı iki basamaklı degilse imha ediyor.
# iki basamaklı ise sayının rakamlarının toplamı ile carpımı birbirine eşit ise mektbu teslim ediyor.
#kosulu saglamyorsa mektubu imha ediyor.
baslık=int(input("mektubun baslıgı kac kelime var:"))
a=baslık//10
if a==0 & a>=10:
    print("mektup imha edildi")
else:
    deger=baslık%10
    toplam=a+deger
    carpim=a*deger
if baslık==(toplam+carpim):
    print("mektup teslim edildi ")
else:
    print("mektup imha edildi")
    
