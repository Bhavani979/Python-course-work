
n=int(input("enter the range:"))
count=0
'''Using loops'''
for i in range(1,n+1):
    if i%3==0:
        count+=1
print(count)

'''Without using loops'''
print(n//3)