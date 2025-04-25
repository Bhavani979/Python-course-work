def load(l):
    for i in l:
        yield i

l=[1,2,3,4,5,6,7,8,9,10]
s=load(l)
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))