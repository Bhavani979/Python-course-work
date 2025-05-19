class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    def to_fahrenheit(self):
        return (self.celsius*9/5)+32
    def to_celsius(self,fahrenheit):
        return (fahrenheit-32)*5/9
temp=Temperature(80)
print(f"Fahrenheit:",temp.to_fahrenheit())
print(f"Celsius:",temp.to_celsius(100))
        