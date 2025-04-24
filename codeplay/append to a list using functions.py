def appendtolist(l,b):
    l.append(b)
    return l

l=list(map(int,input("enter the numbers:").split()))
b=int(input("enter the number to be appended:"))
print(appendtolist(l,b))