def UpdateDictionaryValue(d,k,v):
   d[k]=v
   return d

d=eval(input("Enter dictionary:"))
k=input("Enter key :")
v=input("Enter value:")
print(UpdateDictionaryValue(d,k,v))
