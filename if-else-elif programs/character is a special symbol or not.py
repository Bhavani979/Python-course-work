
char = input("Enter a  character: ")
if len(char) == 1 and not char.isalnum():
    print(f"'{char}' is a special symbol")
else:
    print(f"'{char}' is not a special symbol")