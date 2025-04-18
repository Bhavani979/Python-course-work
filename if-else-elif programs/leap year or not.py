while True:
 n=int(input("enter the number(enter 0 to exit):"))
 if n!=0:
     if n%400==0 or n%4==0 and n%100!=0:
         print("it is leap year")
     else:
         print("it is not leap year")
 else:
      break

