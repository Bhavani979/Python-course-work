def shoot(n):
    if n==0:
        return "game over"
    print(n,"bullets are left")
    return shoot(n-1)
print(shoot(10))