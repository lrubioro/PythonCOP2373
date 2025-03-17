# Lory Rubio Programming Assignment 9
# This program has a BankAcct Class that contains at least the following state information: name, account number, amount and interest rate.
# In addition to an __init__ method, the class also supports methods for adjusting the interest rate, for withdrawing and depositing, and for giving a balance.
# The __str__ method displays balances and interest amounts. A test function  tests the different methods in the BankAcct Class.

#First create the class, and store info
class BankAcct:
    def __init__ (self,name,account_number,amount,rate):
        self.name = name
        self.account_number = account_number
        self.amount = float(amount)
        self.rate = float(rate)

#Create a method to adjust the interest rate
    def adjust_rate (self, rate_new):
        self.rate = float(rate_new)

#Method for withdrawing
    def withdraw (self, amount):

        #if then statement to check if the is enough money in the account and then notifying the user of the action
        if amount <= self.amount:
            self.amount -= amount
            print("Your withdraw was succesful!")
        else:
            print("You do not have sufficient funds")

#Method to deposiut money
    def deposit (self,amount):
        self.amount += amount
        print("Deposit successful")

#Method to get the current balance
    def get_balance(self):
        return self.amount

#Method to calculate interest
    def calculate_interest(self, days):
        interest = self.amount * (self.rate / 100) * (days / 365)
        return interest

#Print results using the __str__ method
    def __str__(self):
        return f"Account owner: {self.name}, Account number: {self.account_number}, Balance: ${self.amount}, Interest rate: {self.rate}%"\

#TEST FUNCTIONS

def test_account():
    # reating a BankAcct instance to gather input form "user"
    name = input("What is the account holder's name? ")
    account_number = input("Enter the account number: ")
    amount = input("Enter the account's balance: ")
    rate = input("Enter the interest rate: ")

    account = BankAcct(name, account_number, amount, rate)

    #Print the info using the __str__ method
    print(account)

    #Test  each  method inidvidually
    deposit_amount = float(input("Enter amount to deposit: "))
    account.deposit(deposit_amount)
    print("New balance:", account.get_balance())

    #Test withdraw method
    withdraw_amount = float(input("Enter amount to withdraw: "))
    account.withdraw(withdraw_amount)
    print("New balance:", account.get_balance())

    #Test
    new_interest_rate = float(input("Enter the new interest rate: "))
    account.adjust_rate(new_interest_rate)
    print("new interest rate:", account.rate)

    #Test calculating interest
    days = int(input("Enter the number of days to calculate interest: "))
    interest = account.calculate_interest(days)
    print("Interest for", days, "days:", interest)

#Call and run the test function
test_account()