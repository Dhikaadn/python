
#python
#kamus global
g_onoff = False

#Algoritma nyalakan TV
def nyalakanTV():
    global g_onoff
    g_onoff = True

#Program utama
def main():
    nyalakanTV()
    print(g_onoff)


main()
    
