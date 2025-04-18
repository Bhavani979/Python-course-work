while True:
    n = input("Enter a number (or '0' to exit): ")
    if n == '0':
        break
    if n.isdigit():
        print(f"'{n}' is a digit")
    else:
        print(f"'{n}' is not a digit")
   