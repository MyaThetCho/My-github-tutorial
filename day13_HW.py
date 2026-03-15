Account = [
    ["Alice", "pw123"], # ID=001
    ["Bob", "123pw"], # ID=002
    ["Charlie", "12pw3"] # ID=003
]

AccDetails = [
    [250.00, 100.00, 200.00],  
    [500.00, 250.00, 300.00],  
    [100.00, 50.00, 100.00]
]

IDs = {
    "001" : 0,
    "002" : 1,
    "003" : 2
}


def Menu(id):
    while True:
        print("\n--- Menu ---")
        print("1. Display balance")
        print("2. Withdraw money")
        print("3. Deposit money")
        print("4. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            Balance(id)
        elif choice == "2":
            Withdraw(id)          
        elif choice == "3":
            Deposit(id)
        elif choice == "4":
            print("Thank you for using our service!")
            break
        else:
            print("Invalid choice")


def Balance(id):
    print(f"Balance : {AccDetails[id][0]}")
    return AccDetails[id][0]
    

def Withdraw(id):
    amt = float(input("Enter amount to withdraw : "))
    overdraft = AccDetails[id][1]
    limit = AccDetails[id][2]
               
    if amt > limit:
        print("Can't Withdraw! Withdrawal exceeds limit.")
    elif amt > Balance(id) + overdraft:
        print("Can't Withdraw! Withdrawal exceeds overdraft limit.")
    else:
        AccDetails[id][0] -= amt
        print(f"Withdraw Successful! Your Balance : {Balance(id)}")
    
    
def Deposit(id):
    amt = float(input("Enter amount to deposit : "))
    AccDetails[id][0] += amt
    print(f"Deposit Successful! Your Balance : {Balance(id)}")
    
  


acc_id = input("Enter you ACC ID : ")
if acc_id not in IDs:
    print("Invalid Acc ID.")
    
id = IDs[acc_id]
name = input("Enter username : ")
pw = input("Enter password : ")
    
if Account[id][0] == name and Account[id][1] == pw:
    print("Login Successful!")
    Menu(id)
else:
    print("Wrong username or password. Login Failed!")
        
    


