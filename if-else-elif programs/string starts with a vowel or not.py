while True:
    str=input("enter the input(enter done to exit):").lower()
    if str!="done":
       print("1.using membership")
       print("2.using conditions")
       approach=int(input("select the approach:"))
       if approach==1:
          vol="aeiou"
          if len(str)>0 and str[0] in vol:
            print("Starts with a vowel")
          else:
             print("Not Starts with a vowel")

       elif approach==2:
            if str[0]=="a" or str[0]=="e" or str[0]=="i" or str[0]=="o" or str[0]=="u":
                print("Starts with a vowel")
            else:
                print("Not Starts with a vowel")
       else:
            print("Invalid option")

    else:
        break
