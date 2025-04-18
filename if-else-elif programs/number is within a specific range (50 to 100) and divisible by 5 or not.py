while True:
    n=int(input("enter the input(enter 0 to exit):"))
    
    if 50 < n < 100:
        print("1.str")
        print("2.condition")
        approach=int(input("select the approach:"))
        if approach==1:
           if len(str(n))==2 and n%5==0:
            print("In range and divisible by 5")
           else:
            print("Doesn't meet both conditions")
        elif approach==2:
        
           if n%5==0:
            print("In range and divisible by 5")
           else:
            print("Doesn't meet both conditions")
        else:
            print("Invalid option")
    else:
            break
            


