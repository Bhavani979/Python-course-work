while True:
  a,b,c=map(int,input("enter the numbers:").split())
  if (a>b+c) and (b>a+c) and (c>a+b):
    print("valid triangle")
  else:
    print("not a valid traingle")