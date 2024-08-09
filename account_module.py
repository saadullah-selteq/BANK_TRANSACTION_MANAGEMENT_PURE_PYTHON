# account.py
from datetime import datetime
from utils import hash_pin

class Account:
    """
    this class will be responsible for :
      Deposit : Responsible for deposit amount to the account,
      Transfer : This module transfer amount from one user to another,
      check_balance: Check the balance of account,
       print_statement : shows all the transaction history,
       withdraw: Withdraw amount from the account,
       set_pin : this module change the previous pin and used hash function.
       
       
      """
    def __init__(self, username, pin, balance=0, transactions=None, is_frozen=False, transaction_limit=1000):
        self.username = username
        self.pin = hash_pin(pin) if len(pin) < 64 else pin  # pin is already hashed if it's 64 characters long
        self.balance = balance
        self.transactions = transactions if transactions is not None else []
        self.is_frozen = is_frozen
        self.transaction_limit = transaction_limit
#Deposit Module
    def deposit(self, amount):
        if self.is_frozen:
            print("Account is frozen.")
            return
        self.balance += amount
        self.transactions.append({'type': 'deposit', 'amount': amount, 'date': str(datetime.now())})
        print(f"Deposited {amount}. New balance: {self.balance}")
#Check balance module
    def check_balance(self):
        print(f"Current balance: {self.balance}")
#print statement module
    def print_statement(self):
        print(f"Account Statement for {self.username}")
        for transaction in self.transactions:
            print(transaction)
#transfer module
    def transfer(self, amount, recipient):
        if self.is_frozen:
            print("Account is frozen.")
            return
        if amount > self.transaction_limit:
            print("Transaction limit exceeded.")
            return
        if self.balance < amount:
            print("Insufficient funds.")
            return
        self.balance -= amount
        recipient.balance += amount
        self.transactions.append({'type': 'transfer', 'amount': amount, 'to': recipient.username, 'date': str(datetime.now())})
        recipient.transactions.append({'type': 'transfer', 'amount': amount, 'from': self.username, 'date': str(datetime.now())})
        print(f"Transferred {amount} to {recipient.username}. New balance: {self.balance}")
#withdraw module
    def withdraw(self, amount):
        if self.is_frozen:
            print("Account is frozen.")
            return
        if self.balance < amount:
            print("Insufficient funds.")
            return
        self.balance -= amount
        self.transactions.append({'type': 'withdraw', 'amount': amount, 'date': str(datetime.now())})
        print(f"Withdrew {amount}. New balance: {self.balance}")
# set pin module
    def set_pin(self, new_pin):
        self.pin = hash_pin(new_pin)
        print("PIN updated successfully.")
