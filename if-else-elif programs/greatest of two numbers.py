'''while True:
    
    num1=int(input("enter a num1(enter 0 to exit):"))
    num2=int(input("enter a num2(enter 0 to exit):"))
    if (num1!=0 and num2!=0):
        if(num1>num2):
          print("num1 is greater than num2")
        else:
          print("num2 is greater than num1")

    else:
         break
         '''
while True:
  num1,num2=input("enter the 2 numbers(enter stop to exit):").split()
  if num1!='stop':
    print("1.greatest")
    print("2.smallest")
    approach=int(input("select approach:"))
    if approach==1:
      if (int(num1)>int(num2)):
         print("num1 is greatest")
      else:
         print("num2 is greatest")
    elif approach==2:
      if (int(num1)<int(num2)):
         print("num1 is smallest")
      else:
        print("num2 is smallest")
  else:
         break
        
        

