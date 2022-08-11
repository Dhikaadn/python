print("Deret")
def aritmetika(a,b,c):
	lst=[]
	for i in range(a,b,c):
		lst.append(i)
	return lst
awal = 1
akhir = 20
sls = 2
deret = aritmetika(awal,akhir,sls)
print("Deret: ",deret)