n = int(input())
#Algoritma
for i in range(n):
    t = int(input())
    r = 1
    i = 2
    while i <= t:
        r *= i # ini sama dengan r=r*i
        i += 1 # ini sama dengan i=i*1
    print(r)
