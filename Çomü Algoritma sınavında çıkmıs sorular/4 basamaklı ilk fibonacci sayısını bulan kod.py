#4 basamaklı ilk fibonacci sayısını bulan kod
fib1=1
fib2=1
i=2
fib=0
while fib<10**999:
    fib=fib1+fib2
    fib1=fib2
    fib2=fib
    i=i+1
print(i)
