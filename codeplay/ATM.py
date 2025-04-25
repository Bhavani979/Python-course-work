data={"balance":50000,"transaction":[]}

def withdraw(amount):
    if amount<=data["balance"]:
      data["balance"]-=amount
      data['transaction'].append(f'{amount} withdrawn from your account.')
      print("Amount is succesfully withdrawn.")
def depoist(amount):
   data["balance"]+=amount
   data["transaction"].append(f"{amount} depoist for your account .")
   print(f"{data["balance"]} is dipoist your account")
def Check_Balance():
    print(f"Your current balance is {data['balance']}")
  
def view_transaction():
    for i in data['transaction']:
        print(i)
print("welcome to ATM")

while True:
   print(f"1.withdraw\n2.depoist\n3.Check_Balance\n4.view_transaction\n5.exit")
   option=int(input("enter the selection (1-5):"))
   if (option==1):
      amount=int(input("enter the withdraw amount :"))
      withdraw(amount)
   elif(option==2):
        amount=int(input("enter the depoist amount :"))
        depoist(amount)
   elif(option==3):
        Check_Balance()
   elif(option==4):
       view_transaction()
   elif(option==5) :
       print("see you later")
       break  
   else:
       print("Try Again")

"""WITHOUT USING FUNCTIONS
#creating user credentials
user_name = "bhavani" #user name
user_password = "bhavani12" #user password

#taking user inputs
customer_name = input("Enter your name: ") #customer name
customer_password = input("Enter your password: ") #customer password

#checking valid customer or not 
if (customer_name == user_name and customer_password == user_password):
    print("Welcome to bank") #greating
    amount = 1000
    
    while True: #while loop for loopeing contusely untill get exit
        print("\n1. Deposit\n2. Withdraw\n3. Mini Statement\n4. Exit") #menu
        option = int(input("Enter your choice (1-4): ")) #user input
        
        if (option == 1):
            deposit = int(input("Enter amount to deposit: "))
            amount += deposit
            print("Your transaction is successful")
            print("Total amount:", amount)
           
        elif (option == 2):
            withdraw = int(input("Enter amount to withdraw: "))
            if (amount >= withdraw):
                amount -= withdraw
                print("Your transaction is successful")
                print("Total amount:", amount)
            else:
                print("Insufficient Funds")
                
        elif (option == 3):
            print("Account Holder:", user_name)
            print("Current Balance:", amount)
            
        elif (option == 4):
            print("Thank you for choosing us")
            break
            
        else:
            print("Invalid option. Please try again.")
            
else:
    print("Invalid credentials")
"""