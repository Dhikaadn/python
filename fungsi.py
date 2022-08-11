dm = 50 
r = 25
tg = 100

#Fungsi
def volumetabung():
    v = 3.14*r*r*tg
    return v
v = volumetabung()
print("volume tabung : ",v,"cm^3")

#Prosedur
def volumetabung():
    print("Volume tabung: ",3.14*r*r*tg,"cm^3")
volumetabung()

#Fungsi
def luasselimuttabung():
    ls = 2*3.14*r*tg
    return ls
ls = luasselimuttabung()
print("Luas selimut tabung : ",ls,"cm^2")

#Prosedur
def luasselimuttabung():
    print("Luas selimut tabung: ",2*3.14*r*tg,"cm^2")
luasselimuttabung()

