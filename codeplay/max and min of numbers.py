l=list(map(int,input("enter the list:").split()))
maxl=l[0]
minl=l[0]
for i in range(1,len(l)):
   if l[i]>maxl:
      maxl=l[i]
   if l[i]<minl:
      minl=l[i]
print("Maximum:",maxl)
print("Minimum:",minl)