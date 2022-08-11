x = int(input())#input x
y = int(input())#input y
if x > y:
    smaller = y #suatu kondisi jika x lebih besar dari y,maka smaller = y
else:
    smaller = x #begitupun sebaliknya
for i in range(1, smaller+1): #terdapat i yang dimulai dari 1
    if((x % i == 0) and (y % i == 0)):#kondisi jika angka sama
        z= i
print(z)
