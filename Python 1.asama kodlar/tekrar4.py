#n.fibonacci sayisi
n=int(input("kacinci fibonnaci sayisini ogrenmek istersiniz? "))
fib1=1
fib2=1
fib=0
for i in range(3,n+1):
    fib=fib1+fib2
    fib1=fib2
    fib2=fib
print (i,".fibonnaci sayisi= ", fib)
