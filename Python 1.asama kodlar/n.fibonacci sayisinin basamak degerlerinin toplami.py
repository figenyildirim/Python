#n.fibonacci sayısını ve bu sayının rakamları toplamını bulan kod
n=int(input("bir sayi girin:"))
fib1=1
fib2=1
fib=0
a=1
b=0
toplam=0
for i in range(2,n):
    fib=fib1+fib2
    fib1=fib2
    fib2=fib
sayi=fib
while a!=0:
    a=fib//10
    b=fib%10
    toplam=toplam+b
    fib=a
print(sayi, toplam)

