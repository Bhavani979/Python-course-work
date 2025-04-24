''' USING BUILT FUNCTION

def lengthofstring(l):
    return len(l)
l=input("enter the name:")
print(lengthofstring(l))
'''



def lengthofstring(l):
    count=0
    for i in l:
        count+=1
    return count
l=input("enter the name:")
print(lengthofstring(l))