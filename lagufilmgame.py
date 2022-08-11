print("Selamat Datang silahkan ketik menu dibawah ini!")
print("Ketik dengan huruf kecil yaaa")
a = str(input("lagu(l),game(g),film(f): "))
r = "y"

if (a=="l"):
    y = str(input("Lagu apa yang ingin anda putar?"))
    if (y=="sofia clairo"):
        print("lagu yang sangat bagus ferguso")
    elif(y=="figurinha"):
        print("itu lagu favoritmu pasti")
    else:
        print("cari lagu lagi yang lain!!!")

elif (a=="g"):
    x = str(input("Game apa yang ingin anda mainkan?"))
    if (x=="tekken"):
        print("Game bagus")
    elif (x=="basara"):
        print("Game cupu")
    else:
        print("Cari game lain")

elif (a=="f"):
    x = str(input("Film apa yang ingin anda tonton?"))
    if (x=="chaki"):
        print("film horror itu")
    elif (x=="avatar"):
        print("film anak anak")
    else:
        print("Cari film lain!!!")

else:
    print("Menu yang tidak tersedia disini")

while r=="y":
    r = str(input("Ingin masuk menu lagi?(y/t)"))
    if r=="y":
        a = str(input("lagu(l),game(g),film(f): "))
        if (a=="l"):
            y = str(input("Lagu apa yang ingin anda putar?"))
            if (y=="sofia clairo"):
                print("lagu yang sangat bagus ferguso")
            elif(y=="figurinha"):
                print("itu lagu favoritmu pasti")
            else:
                print("cari lagu lagi yang lain!!!")

        elif (a=="g"):
            x = str(input("Game apa yang ingin anda mainkan?"))
            if (x=="tekken"):
                print("Game bagus")
            elif (x=="basara"):
                print("Game cupu")
            else:
                print("Cari game lain")

        elif (a=="f"):
            x = str(input("Film apa yang ingin anda tonton?"))
            if (x=="chaki"):
                print("film horror itu")
            elif (x=="avatar"):
                print("film anak anak")
            else:
                print("Cari film lain!!!")

        else:
            print("Menu yang tidak tersedia disini")
    elif r=="t":
        print("Terima kasih")
    else:
        print("y/t njing")
        


