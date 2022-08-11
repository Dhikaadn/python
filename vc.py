a = [[1,2,3],
    [4,5,6]]
b = [[7,8,9],
    [10,11,12]]
jml=[]

print('a=',a)
print('b=',b)
for x in range(len(a)):
    jml.append([])
    for y in range(len(a[0])):
        jml[x].append(a[x][y]+b[x][y])
print('a+b=',jml)
        
    
