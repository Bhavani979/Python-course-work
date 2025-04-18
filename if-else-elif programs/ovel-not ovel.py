while True:
    n=input("enter the input(enter done to exit):")
    if n!="done":
       print("1.using membership")
       print("2.using conditions")
       approach=int(input("select the approach:"))
       if approach==1:
          vol="aeiou"
          if n in vol:
            print("it is vowel")
          else:
             print("it is not vowel")

       elif approach==2:
            if n=="a" or n=="e" or n=="i" or n=="o" or n=="u":
                print("it is vowel")
            else:
                print("it is not vowel")
       else:
            print("Invalid option")

    else:
        break