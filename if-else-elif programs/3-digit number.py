while True:
    n=int(input("enter the input(enter 0 to exit):"))
    print("1.str")
    print("2.condition")
    approach=int(input("select the approach:"))

    if n!=0:

     if approach==1:
        if len(str(n))==3:
            print("it is 3-digit number")
        else:
            print("it is not 3-digit number")
            
     if approach==2:
        
        if n>99 and n<1000 :
            print("it is 3-digit number")
        else:
            print("it is not 3-digit number")
     else:

          print("Invalid option")


    else:
         break
