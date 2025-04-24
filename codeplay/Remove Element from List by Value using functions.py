def removeelementfromlist(l):
    l.remove(a)
    return l
l=list(map(int,input("enter the elements:").split()))
a=int(input("enter the number:"))
print(removeelementfromlist(l))