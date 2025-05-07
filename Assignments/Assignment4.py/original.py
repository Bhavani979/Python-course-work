
import programs
def display():
    return '''
1.characterisconsonant
2.leapyear
3.lengthofstrings
4.numcheck
5.triangle
6.threedigitnum
7.angle
8.multipleoften
9.frequencyofelements
10.uppercase
11.numiszero
12.negativeandodd
13.stringsareequal
14.commonelements
15.squareofnum
16.evennumbers
17.lengthofpassword
18.divisibleby3and7
19.characterisspecialsymbol
20.greatestofthreenumbers
'''
while True:
 print(display())
 op=int(input("Enter the number(0-exit):"))
 if op==1:
   print(programs.characterisconsonant())
 elif op==2:
  print(programs.leapyear())
 elif op==3:
  print(programs.l_s())
 elif op==4:
   print(programs.numcheck())
 elif op==5:
   print(programs.triangle())
 elif op==6:
   print(programs.threedigitnum())
 elif op==7:
   print(programs.angle())
 elif op==8:
   print(programs.multipleoften())
 elif op==9:
   print(programs.frequencyofelements())
 elif op==10:
   print(programs.uppercase())
 elif op==11:
   print(programs.numiszero())
 elif op==12:
   print(programs.negativeandodd())
 elif op==13:
   print(programs.stringsareequal())
 elif op==14:
   print(programs.commonelements())
 elif op==15:
   print(programs.squareofnum())
 elif op==16:
   print(programs.evennumbers())
 elif op==17:
   print(programs.lengthofpassword())
 elif op==18:
   print(programs.divisibleby3and7())
 elif op==19:
   print(programs.characterisspecialsymbol())
 elif op==20:
   print(programs.greatestofthreenumbers())
  
 elif op==0:

  break