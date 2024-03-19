"""
In this project, I have designed and implement two classes in Python: BasicAccount and PremiumAccount using concepts and principles of object-orientation such as objects and classes, encapsulation, object state, coupling, cohesion and modularity.
"""

import random as R
from datetime import datetime as D

class BasicAccount:
    """Parent Class BasicAccount"""
    count = 0  # Class variable count for generating account number

    def __init__(self, ac_name, opening_balance):
        """Constructor method for BasicAccount class (Parent Class)"""
        BasicAccount.count += 1
        self.name = ac_name
        self.ac_num = BasicAccount.count
        self.balance = opening_balance
        self.card_num = None
        self.card_exp = None

    def __str__(self):
        """String representaion"""
        return ("Account Holder Name:" + self.name +"\nAvailable Balance:" + str(self.get_available_balance()))

    def deposit(self, amount):
        """Deposite function, which add amount to current account balance if amount is greater than zero otherwise prints invalid amount message"""

        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount entered. Please enter valid amount.")

    def withdraw(self, amount):
        """Withdraw function, which sustract the amount from current account balace if amount is greater than zero and less than available balance
           otherwise print error message"""

        if amount > 0 and amount <= self.get_available_balance():
            self.balance -= amount
            print(self.name + "has withdrawn £"+ str(amount) +". New balance is £" + str(self.get_balance()))
        else:
            print("Can not withdraw £" + str(amount))

    def get_available_balance(self):
        """get_available_balance function, which return current available balance in Basic account"""
        return float(self.balance)

    def get_balance(self):
        """get_available_balance function, which return current available balance of Basic account"""
        return float(self.balance)

    def print_balance(self):
        """print_balance function, which prints the current available balance of Basic account"""
        print("Balance: £" + str(self.get_balance()))

    def get_name(self):
        """get_name function, which returns name of account holder"""
        return self.name

    def get_ac_num(self):
        """get_ac_num function, which returns the account number of account holder"""
        return str(self.ac_num)

    def issue_new_card(self):
        """issue_new_card function, which generate card number and expiry date of that card."""

        card_number=''
        for _ in range(16):
            card_number += str(R.randint(0, 9))  # Generated 16 digit ramdom number for card
        self.card_num=card_number
        now = D.now()
        self.card_exp = (now.month, (now.year + 3) % 100)  # Generated card expiry date as MM/YY format

    def close_account(self):
        """close_account function, which close the account and return back if any balance available to account holder,
           and if balance is less than zero then prints the error message."""

        if self.balance > 0:
            self.withdraw(self.balance)
            return True
        elif self.balance==0:
            return True
        else:
            print("Can not close account due to customer being overdrawn by £" + str(abs(self.balance)))
            return False


class PremiumAccount(BasicAccount):
    """Child Class PremiumAccount, which inherits Parent Class BasicAccount"""
    def __init__(self, ac_name, opening_balance, initial_overdraft):
        """Constructor method for PremiumAccount class"""
        BasicAccount.__init__(self, ac_name, opening_balance)  # Used to inherit methods and functions of parent class BasicAccount
        self.overdraft = True
        self.overdraft_limit = initial_overdraft

    def __str__(self):
        """String representaion"""
        return ("Account Holder Name:" + self.name + "\nAvailable Balance: " + str(self.get_available_balance()) + "\nOverdraft: " + self.overdraft + "\nOverdraft Limit: " + str(self.overdraft_limit))

    def set_overdraft_limit(self, new_limit):
        """set_overdraft_limit function, which update the current overdraft limit with new limit if it is greater than zero."""
        if new_limit >= 0:
            self.overdraft_limit = new_limit
            self.overdraft=True

    def get_available_balance(self):
        """get_available_balance function, which returns the sum of available balance and overdraft limit for Premium account"""
        return float(self.balance + self.overdraft_limit)

    def print_balance(self):
        """print_balance function, which prints the current available balance and overdraft limit of Premium account"""
        print("Balance: £" + str(self.balance) + "Overdraft Limit: £" + str(self.overdraft_limit))

    def close_account(self):
        """close_account function, which close the account and return back if any balance available to account holder,
           and if balance is less than zero then prints the error message."""

        if self.balance > 0:
            self.withdraw(self.balance)
            return True
        elif self.balance==0:
            return True
        else:
            print("Can not close account due to customer being overdrawn by £" + str(abs(self.balance)))
            return False
