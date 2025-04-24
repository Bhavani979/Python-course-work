a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
numbers=[a,b,c]
max_num=numbers[0]
for num in numbers:
    if num>max_num:
        max_num=num
print(f'The maximum number is:', {max_num})