# Illustrative Problem 1

class Customer:
    """A customer of ABC Bank with a checking account. Customers have the following properties:
    
    Attributes:
        name: A string representing the customer's name.
        iden: A string representing the customer's identification number.
        acno: A string representing the customer's account number.
    """
    def __init__(self, name, iden, acno) -> None:
        self.custName = name
        self.custId = iden
        self.custAcno = acno

    def display(self):
        """Display the customer's details."""
        print("Customer Name: ", self.custName)
        print("Customer Id: ", self.custId)
        print("Customer Account Number: ", self.custAcno)

if __name__ == '__main__':
    name = input("Enter Customer Name: ")
    iden = input("Enter Customer Id: ")
    acno = input("Enter Customer Account Number: ")
    cust = Customer(name, iden, acno)
    cust.display()

# Illustrative Problem 2

class Account(Customer):

    """A customer of ABC Bank with a checking account. Customers have the following properties:
    
    Attributes:
        name: A string representing the customer's name.
        iden: A string representing the customer's identification number.
        acno: A string representing the customer's account number.
        actype: A string representing the customer's account type.
        acbal: A string representing the customer's account balance.
    """

    def __init__(self, name, iden, acno, actype, acbal) -> None:
        super().__init__(name, iden, acno)
        self.acType = actype
        self.acBal = acbal

    def deposit(self):
        amount = int(input("Enter the amount to be deposited: "))
        self.acBal += amount
        print("Amount Deposited: ", amount)
        
    def withdraw(self):
        amount = int(input("Enter the amount to be withdrawn: "))
        if self.acBal >= amount:
            self.acBal -= amount
            print("Amount Withdrawn: ", amount)
        else:
            print("Insufficient Balance")
            
    def checkBalance(self):
        print("Balance: ", self.acBal)

    def display(self):
        super().display()

if __name__ == '__main__':
    name = input("Enter Customer Name: ")
    iden = input("Enter Customer Id: ")
    acno = input("Enter Customer Account Number: ")
    actype = input("Enter Customer Account Type: ")
    acbal = int(input("Enter Customer Account Balance: "))
    cust = Account(name, iden, acno, actype, acbal)
    cust.deposit()
    cust.withdraw()
    cust.checkBalance()
    cust.display()


# Illustrative Problem 3

import datetime
class Date:
    def __init__(self,dd,mm,yy) -> None:
        self.dd = dd
        self.mm = mm
        self.yy = yy

    def __checkdate(self):
        try:
            datetime.datetime(self.yy,self.mm,self.dd)
        except ValueError:
            print("Invalid Date")
            exit()

    def display(self):
        print("Date: {}/{}/{}".format(self.dd,self.mm,self.yy))

# Illustrative Problem 4

import datetime
class FindAge:
    def __init__(self,) -> None:
        pass

    def findAge(self, birthDate):
        today = datetime.date.today()
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
        return age