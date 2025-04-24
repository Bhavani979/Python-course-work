def increment(d):
    for k,v in d.items():
        d[k]=v+1
    return d     
d=eval(input("Enter the dictionary:"))
print(increment(d))