grocery={"Apple":20,"Banana":10,"Milk":25}

cart={"Apple":5,"Banana":2,"Milk":1}
print("Grocery Bill: ")
print("--------------")
i=0
for key,value in grocery.items():
  i+=1
  print(f'{i}. {key} - ₹{value}')

s=0
d=10
for key,value in cart.items():
  print(f'{key} Bought: {value} * {grocery[key]}= Rs {value*grocery[key]}')
  s+=value*grocery[key]
d=(10/100)*s
final=s-d
print("--"*20)
print(f'total bill : {s}')
print(f'discount applied:{d}')
print(f'final amount to pay:{final}')
k=input("enter the item to check:")
print(f'item availability check:{k}')
if k in grocery:
   print("Available in grocery?:True")
else:
  print("Available in grocery?:False")
