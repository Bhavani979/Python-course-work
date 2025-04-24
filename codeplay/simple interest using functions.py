def simpleinterest(p,r,t):
    return (p*t*r)/100
p,r,t= map(int,input("enter the numbers:").split())
print(simpleinterest(p,r,t))