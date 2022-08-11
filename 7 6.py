t = int(input("banyak testcase: "))
i = 1
while(i<=t):
    print("testcase",i)
    a = int(input("angka korek: "))
    if(a>=0) and (a<=9):
        if a==0 or a==6 or a==9:
            print("korek yang dibutuhkan = 6")
        elif a==1:
            print("korek yang dibutuhkan = 2")
        elif a==2 or a==3 or a==5:
            print("korek yang dibutuhkan = 5")
        elif a==4:
            print("korek yang dibutuhkan = 4")
        elif a==7:
            print("korek yang dibutuhkan = 3")
        elif a==8:
            print("korek yang dibutuhkan = 7")
    else:
        print("korek 0-9")
        i+=1
        
        

                  
        

        

        
    
        
                      
          
          
        
            
            
          
