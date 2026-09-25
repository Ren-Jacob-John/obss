class bank:
    def __init__(self, ID, number, ifsccode, minimumbalance):
        self.ID = ID
        self.number = number
        self.ifsccode = ifsccode
        self.minimumbalance = minimumbalance
    def display(self):
        print(f"Customer ID:{self.ID}")
        print(f"Account Number:{self.number}")
        print(f"IFSC Code:{self.ifsccode}")
        print(f"Minimum Balance:{self.minimumbalance}")
n = int(input("Enter the Number of Customers:"))
for i in range(0, n):
    ID = int(input("Enter the Customer ID: "))
    number = int(input("Enter the Account Number: "))
    ifsccode = input("Enter the IFSC Code: ")
    minimumbalance = float(input("Enter the Minimum Balance: "))
    customers = bank(ID, number, ifsccode, minimumbalance)
    print(f"Details of Customer {i}")
    customers.display()