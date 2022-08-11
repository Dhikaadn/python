from Globals9 import*

def CheckOnOff():
    global g_onoff
    return g_onoff
''' langsung mengembalikan global g_onoff
'''
    
def TurnOnoff():
    global g_onoff
    if CheckOnOff()==True:
        print("AC mati")#Jika hidup
        g_onoff=False#dimatikan
    else:
        print("AC hidup")
        g_onoff=True
        Display()
    
''' Jika CheckOnOff() bernilai true maka global g_onoff diberi
nilai False, selain itu global g_onoff diberi nilai True
'''
def TempUp():
    global g_temp
    if CheckOnOff()==True:
        if g_temp<28:
            g_temp=g_temp+1
            Display()
        else:
            print("suhu maksimal")
    else:
        print("AC masih mati")
''' Menaikkan temperatur suhu hanya 1 derajat per pemanggilan
prosedur ini. Update nilai global g_temp dengan g_temp+1
Initial state (syarat prosedur ini bekerja): CheckOnOff()
bernilai true
'''
def TempDown():
    global g_temp
    if CheckOnOff()==True:
        if g_temp>18:
            g_temp=g_temp-1
            Display()
        else:
            print("suhu minimum")
    else:
        print("AC masih mati")
        
''' Menurunkan temperatur suhu hanya 1 derajat per pemanggilan
prosedur ini. Update nilai global g_temp dengan g_temp-1
Initial state (syarat prosedur ini bekerja): CheckOnOff()
bernilai true
'''
def FanSpeed():
    global g_fanlevel
    if CheckOnOff()==True:
        if g_fanlevel<4:
            g_fanlevel=g_fanlevel+1
        else:
            g_fanlevel=1
            Display()
    else:
        print("AC masih mati")
''' Menaikkan nilai level kipas, namun demikian, jika level
kipas sudah mencapai batas maksimum yaitu 4, maka level
kipas akan menjadi 1, update nilai global g_fanlevel
Initial state (syarat prosedur ini bekerja): CheckOnOff()
bernilai true
'''
def PowerChill():
    global g_temp
    global g_fanlevel
    if CheckOnOff()==True:
        g_temp=18
        g_fanlevel=4
        Display()
    else:
        print("AC masih mati")
''' Langsung memberikan nilai g_temp dengan nilai terendah dan
g_fanlevel dengan nilai tertinggi.
Initial state (syarat prosedur ini bekerja): CheckOnOff()
bernilai true
'''
def Display():
    global g_temp
    global g_fanlevel
    if CheckOnOff()==True:
        print("Temperature:",g_temp)
        print("Fan Speed:",g_fanlevel)
    else:
        print("AC masih mati")
''' Mengoutputkan status suhu dan level kipas saat ini.
Yang dioutputkan adalah g_temp dan g_fanlevel.
Initial state (syarat prosedur ini bekerja): CheckOnOff()
bernilai true
'''
