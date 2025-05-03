class evenorodd:
    def __init__(self,num):
        self.num=num
    def check(self):
        if self.num%2==0:
            return "even number"
        else:
            return "odd number"
while True:
    n=int(input("Enter the number(0-Exit):"))
    if n!=0:
        ch=evenorodd(n)
        print(ch.check())
    else:
        break
    