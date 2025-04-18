while True:
    password = input("Enter your password: ")
    
    if len(password) >= 8:
        print("Password is strong (8+ characters)")
    else:
        print("Password is weak (less than 8 characters)")