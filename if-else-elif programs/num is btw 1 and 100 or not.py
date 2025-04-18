while True:
    n=int(input("enter the input(enter 0 to exit):"))
    
    if 1<n<100:
        print("1.str")
        print("2.condition")
        approach=int(input("select the approach:"))
        if approach==1:
           if len(str(n))==1 or len(str(n))==2:
            print("In range")
           else:
            print("Is not in range")
        elif approach==2:
        
           if n>1 and n<100 :
            print("In range")
           else:
            print("Is not in range")
        else:
            print("Invalid option")
    else:
            break
            
