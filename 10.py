def cekduakatasama(s1,s2):
    return s1==s2

def carikarakter(s,c):
    temp = False
    for char in s:
        if char==s:
            temp=True
    if temp:
        print("ketemu")
    else:
        print("tidak ketemu")

#pu
def main():
    s1 = input()
    s2 = input()
    print(cekduakatasama(s1,s2))
    carikarakter(s1,"a")
main()
            
