while True:
    n=int(input("enter the input(enter 0 to exit):"))
    if n%100==0:
        if n%400==0 :
            print(f"{n} is a century year and a leap year")
        else:
            print(f"{n} is  a century year and not a leap year")
    else:
        if n%4==0 :
          print(f"{n} is a leap year and not a century year")
        else:
         print(f"{n} neither a leap year nor a century year")