n=tuple(map(int,input("Enter the elements:").split()))
sum=0
for i in n:
    if i%2!=0:
        sum=sum+i
        print(i)
print(sum)
