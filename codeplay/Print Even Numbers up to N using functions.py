def evennum(n):
    for i in range(1,n+1):
        if i%2==0:
            print(i)
    return ""
n=int(input("enter the number:"))
print(evennum(n))