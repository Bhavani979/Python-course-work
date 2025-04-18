while True:
    age1 = int(input("Enter first age:"))
    age2=int(input("Enter second age: "))
    if age1 > age2:
     print(f"{age1} is older")
    elif age2 > age1:
            print(f"{age2} is older")
    else:
            print(f"Both are the same age")
            