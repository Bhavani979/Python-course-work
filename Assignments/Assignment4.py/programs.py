def characterisconsonant():
    return '''while True:
    chr = input("Enter the input (enter 'done' to exit): ")
    vol = "aeiou"
    if chr == 'done':
        break
    if chr in vol:
        print("Character is not a consonant")
    else:
        print("Character is a consonant")
=============================================================
TESTCASE-1:
input:r
output:Character is a consonant
TESTCASE-2:
input:o
output:Character is not a consonant'''



def leapyear():
    return  '''while True:
    n=int(input("enter the number(enter 0 to exit):"))
    if n!=0:
     if n%400==0 or n%4==0 and n%100!=0:
         print("it is leap year")
     else:
         print("it is not leap year")
    else:
      break
===============================================================
    TESTCASE-1:
    input:2000
    output:it is leap year
    TESTCASE-2:
    input:1800
    output:it is not leap year'''


def l_s():
    
    return '''while True:
  str1=input("enter the input1:")
  str2=input("enter the input2:")
  if len(str1)>len(str2):
    print(f"'{str1}'  is longer")
  elif len(str2)>len(str1):
    print(f"'{str2}' is longer")
  else:
    print("Both strings have equal length")
=================================================================
TESTCASE-1:
input:
str1=pavani
str2=bhavani
output:'bhavani' is longer
TESTCASE-2:
input:
str1=Python is a programming language
str2=I am learning Python
output:'Python is a programming language' is longer
'''

def numcheck():
    return '''while True:
    n=int(input("enter the input:"))
     if n>1 and n<100 :
            print("In range")
     else:
            print("Is not in range")
===============================================================
TESTCASE-1:
input:5
output:In range
TESTCASE-2:
input:0
output:Is not in range'''


def triangle():
    return '''while True:
  a,b,c=map(int,input("enter the numbers:").split())
  if (a>b+c) and (b>a+c) and (c>a+b):
    print("valid triangle")
  else:
    print("not a valid traingle")
================================================================
TESTCASE-1:
input:4 5 6 
output:not a valid traingle
TESTCASE-2:
input:3 4 5
output:valid triangle'''



def threedigitnum():
 return ''' n=int(input("enter the input:"))
        if n>99 and n<1000 :
            print("it is 3-digit number")
        else:
            print("it is not 3-digit number")
===============================================================
TESTCASE-1:
input:100
output:it is 3-digit number
TESTCASE-2:
input:80
output:it is not 3-digit number
     
'''


def angle():
    return '''
while True:
        angle = float(input("Enter angle in degrees:"))
            
        if 0 < angle < 90:
            print(f"{angle}° is an acute angle")
        elif angle == 90:
            print(f"{angle}° is a right angle")
        elif 90 < angle < 180:
            print(f"{angle}° is an obtuse angle")
        else:
            print("Angle must be between 0° and 180°")
==============================================================
TESTCASE-1:
input:80
output:Enter angle in degrees:80
80.0° is an acute angle
TESTCASE-2:
input:120
output:120.0° is an obtuse angle'''


def multipleoften():
    return '''
    num=int(input("enter the number:"))
if (10*num):
    print("is multiple of 10")
else:
    print("not multiple of 10")
===============================================================
TESTCASE-1:
input:100
output:is multiple of 10
input:0
output:not multiple of 10

'''

def frequencyofelements():
    return ''''
    elements=input("enter the elements:").split(" ")
frequency={}
for i in elements:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)
=============================================================
TESTCASE-1:
input:Enter the elements: apple banana apple orange banana apple
output:{'apple': 3, 'banana': 2, 'orange': 1}
TESTCASE-2:
input:Enter the elements: 1 2 3 2 3 1 1
output:{'1': 3, '2': 2, '3': 2}

'''

def uppercase():
    return '''while True:
    ch=input("enter the char:")
    if ch.isupper():
      print("upper")
    else:
       print(" lower")
================================================================
TESTCASE-1:
input:SUNSET
output:upper
TESTCASE-2:
input:flyzone
output:lower
'''


def numiszero():
    return '''num=int(input("enter the input:"))
if (num==0):
    print("number is zero")
else:
    print("number is not zero")
        
================================================================
TESTCASE-1:
input:0
output:number is zero
TESTCASE-2:
input:10
output:number is not zero
'''

def negativeandodd():
    return '''while True:
    num=int(input("enter the num:"))
    if num<0 and num%2!=0:
      print("negative and odd num")
    else:
       print(" not negative and odd num")
===================================================================
TESTCASE-1:
input:56
output:not negative and odd num
TESTCASE-2:
input:-3
output:negative and odd num
'''


def stringsareequal():
    return '''str1=input("enter the input1:")
str2=input("enter the input2:")
if (str1==str2):
    print("Strings are equal")
else:
    print("Strings are not equal")
=======================================================================
TESTCASE-1:
input:
enter the input1:gun
enter the input2:gun
output:Strings are equal
TESTCASE-2:
enter the input1:hyderabad
enter the input2:destination
output:Strings are not equal
'''

def commonelements():
   return''' set1=set(map(int,input("enter the numbers:").split()))
set2=set(map(int,input("enter the numbers:").split()))
common=[]
for i in set1:
    if i in set2:
        common.append(i)
print(common)
=========================================================================
TESTCASE-1:
input:
enter the numbers:1 2 3
enter the numbers:5 6 2
output:[2]
TESTCASE-2:
input:
enter the numbers:1 4 5
enter the numbers:0 9 8
output:[]
        ''' 
 

def squareofnum():
    return '''num=int(input("enter a num:"))
k=int(input("enter k:"))
if num**2==k:
    
    print("k is sqaure of num")
else:
    print("k is not square of num")
======================================================================
TESTCASE-1:
input:
enter a num:25
enter k:625
output:k is sqaure of num
TESTCASE-2:
input:
enter a num:15
enter k:30
output:k is not square of num
    '''


def evennumbers():
    return '''
    n=list(map(int,input("enter the elements:").split()))
even=[]
for i in n:
    if i%2==0:
        even.append(i)
print(even)
=========================================================================
TESTCASE-1:
input:
enter the elements:8 6 9
output:[8, 6]
TESTCASE-2:
input:
enter the elements:5 3 1
output:[]
'''


def lengthofpassword():
    return '''while True:
    password = input("Enter your password: ")
    
    if len(password) >= 8:
        print("Password is strong (8+ characters)")
    else:
        print("Password is weak (less than 8 characters)")
====================================================================
TESTCASE-1:
input:
Enter your password: bhavani@123
output:Password is strong (8+ characters)
TESTCASE-2:
Enter your password: bhavani
Password is weak (less than 8 characters)

'''


def divisibleby3and7():
   return''' while True:
    n=int(input("enter the input(enter 0 to exit):"))
    if n!=0:
        if n%3==0 and n%7==0:
            print("divisible by 3 and 7")
        else:
            print("not divisible by 3 and 7")
    else:
         break
=================================================================
TESTCASE-1:
input:
enter the input(enter 0 to exit):343
output:
not divisible by 3 and 7
TESTCASE-2:
input:
enter the input(enter 0 to exit):42
output:
divisible by 3 and 7
'''


def characterisspecialsymbol():
    return '''char = input("Enter a  character: ")
if len(char) == 1 and not char.isalnum():
    print(f"'{char}' is a special symbol")
else:
    print(f"'{char}' is not a special symbol")
==============================================================
TESTCASE-1:
input:
Enter a  character: @
output:'@' is a special symbol
TESTCASE-2:
input:
enter the input:12
output:'12' is not a special symbol
'''


def greatestofthreenumbers():
    return '''while True:
    num1,num2,num3=map(int,input("enter the numbers:").split())
    if num1>=num2 and num1>=num3:
        print(f'{num1} is the greatest')
    elif num2>=num1 and num2>=num3:
        print(f'{num2} is the greatest')
    else:
        print(f'{num3} is the greatest')
====================================================================
TESTCASE-1:
input:
enter the numbers:60 50 20
output:60 is the greatest
TESTCASE-2:
input:
enter the numbers:40 10 100
output:100 is the greatest
'''