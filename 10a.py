def carikarakter(s,c):
    temp = False
    for char in s:
        if char==s:
            temp=True
            break
    if temp:
        print("ketemu")
    else:
        print("tidak ketemu")

#pu
def main():
    s1 = input()
    s2 = input()
    carikarakter(s1,"a")
    print(cekduakatasama(s1,s2))
main()
            
