#n.fibonaccı sayısının basamak degerleri toplamını bulan kod
n=int(input("lutfen bir sayi girin:"))
fib1=1
fib2=1
toplam=0
a=1
for i in range(3,n+1):
    fib=fib1+fib2
    fib1=fib2
    fib2=fib
c=fib
while a!=0:
    a=fib//10
    deger=fib%10
    toplam=toplam+deger
    fib=a
print(n,".fibonaci sayisi",c,"dir. ve basamak degerleri toplamı", toplam,"dır.")
