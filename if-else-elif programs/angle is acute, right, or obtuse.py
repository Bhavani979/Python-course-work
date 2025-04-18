while True:
        angle = float(input("Enter angle in degrees:"))
            
        if 0 < angle < 90:
            print(f"{angle}° is an acute angle")
        elif angle == 90:
            print(f"{angle}° is a right angle")
        elif 90 < angle < 180:
            print(f"{angle}° is an obtuse angle")
        else:
            print("Angle must be between 0° and 180°")
        