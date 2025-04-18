'''while True:
  n=int(input("enter the  number:"))
  if (n%2==0 or n%3==0) and not(n%2==0 and n%3==0):
    print(f'{n} is divisible by 2 or 3 but not both')
  else:
    print(f"{n} does not satisfy the condition (divisible by neither or both)")
    '''
while True:
    n = int(input("Enter the number: "))
    
    if n % 2 == 0 and n % 3 == 0:
        print(f"{n} is divisible by both 2 and 3")
    elif n % 2 == 0:
        print(f"{n} is divisible by 2")
    elif n % 3 == 0:
        print(f"{n} is divisible by 3")
    else:
        print(f"{n} is not divisible by 2 or 3")