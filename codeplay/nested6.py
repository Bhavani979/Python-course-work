n=int(input("enter the size:"))
for i in range(n):
    for k in range(n-i,0,-1):
        print(' ',end='')
    for j in range(i+1):
       print('*',end='')
    
    print()
   