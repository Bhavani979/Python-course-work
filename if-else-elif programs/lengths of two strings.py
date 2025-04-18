while True:
  str1=input("enter the input1:")
  str2=input("enter the input2:")
  if len(str1)>len(str2):
    print(f"'{str1}'  is longer")
  elif len(str2)>len(str1):
    print(f"'{str2}' is longer")
  else:
    print("Both strings have equal length")