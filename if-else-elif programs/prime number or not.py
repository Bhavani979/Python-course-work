while True:
     n=int(input("enter a number:"))
     isPrime=0
     for i in range(2,(n//2)+1):
         if n%i==0:
             isPrime+=1

     if isPrime==0:
         print("Prime number")
     else:
         print("Not a prime number")
