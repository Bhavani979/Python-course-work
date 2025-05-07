def countvowels(s):
    vol="aeiouAEIOU"
    count=0
    for i in s:
     if i in vol:
      count=count+1
    return count
s=input("enter the input:")
print(countvowels(s))