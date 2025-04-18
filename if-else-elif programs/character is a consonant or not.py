while True:
    chr=input("enter the input(enter done to exit):")
    if chr!="done":
       print("1.using membership")
       print("2.using conditions")
       approach=int(input("select the approach:"))
       if approach==1:
          vol="aeiou"
          if chr in vol:
            print("character is not consonant")
          else:
             print("character is a consonant")

       elif approach==2:
            if chr=="a" or chr=="e" or chr=="i" or chr=="o" or chr=="u":
                print("character is not consonant")
            else:
                print("character is a consonant")
       else:
            print("Invalid option")

    else:
        break
