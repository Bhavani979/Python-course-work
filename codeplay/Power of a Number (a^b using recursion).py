def power(a,b):
  if b==0:
    return 1
  else:
    return a*power(a,b-1)
a,b=map(int,input("Enter base and exponent:").split())
print(power(a,b))