def returnlistofsquares(l):
    squarelist=[]
    for i in l:
        squarelist.append(i**2)
    return squarelist
l=list(map(int,input("enter the list elements:").split()))
print(returnlistofsquares(l))