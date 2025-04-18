while True:
    n=int(input("enter the input(enter 0 to exit):"))
    if n!=0:
        if n%3==0 and n%7==0:
            print("divisible by 3 and 7")
        else:
            print("not divisible by 3 and 7")
    else:
         break
    
