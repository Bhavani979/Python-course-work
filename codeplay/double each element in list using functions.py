def double(l):
    for i in range(len(l)):
        l[i]=l[i]*2
    return l      
l=list(map(int,input("enter the numbers:").split()))
print(double(l))