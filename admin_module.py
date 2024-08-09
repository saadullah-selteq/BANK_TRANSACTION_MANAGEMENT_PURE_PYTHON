import json
import os
from account_module import Account
from utils import load_data, save_data, hash_pin

class Admin:
           """   this class will be responsible for :
      create_account : Responsible for create the account of the user,
      show_details : show all the details of the accounts ,
      delete_account: Admin can delete tyhe registered account,
       show_transactions : shows all the transaction history,
       freeze_account: this module freeze the account and no transaction can be performed,
       set_transaction_limit : this module can increrase the transaction limit of the user ,
       generate_reports: generate the report of the transaction history,
       save_accounts: its shows the registered account information 
       
       """
       
def __init__(self, data_file='accounts.json'):
        self.accounts = load_data(data_file)
        self.data_file = data_file
#Create account module
def create_account(self, username, pin):
        if username in self.accounts:
            print("Username already exists.")
            return
        self.accounts[username] = Account(username, pin).__dict__
        self.save_accounts()
        print("Account created successfully.")
#show details module
def show_details(self, username):
        if username not in self.accounts:
            print("Account not found.")
            return
        account = self.accounts[username]
        print(f"Username: {username}, Balance: {account['balance']}, Frozen: {account['is_frozen']}")
# show transactin module
def show_transactions(self, username=None):
        if username:
            if username not in self.accounts:
                print("Account not found.")
                return
            print(f"Transactions for {username}: {self.accounts[username]['transactions']}")
        else:
            for user, account in self.accounts.items():
                print(f"Transactions for {user}: {account['transactions']}")
#delete account module
def delete_account(self, username):
        if username not in self.accounts:
            print("Account not found.")
            return
        del self.accounts[username]
        self.save_accounts()
        print("Account deleted successfully.")
#freeze account module
def freeze_account(self, username):
        if username not in self.accounts:
            print("Account not found.")
            return
        self.accounts[username]['is_frozen'] = True
        self.save_accounts()
        print("Account frozen successfully.")
#set transaction_limit module
def set_transaction_limit(self, username, limit):
        if username not in self.accounts:
            print("Account not found.")
            return
        self.accounts[username]['transaction_limit'] = limit
        self.save_accounts()
        print("Transaction limit set successfully.")
#generate report module
def generate_reports(self):
        cash_in, cash_out = 0, 0
        for account in self.accounts.values():
            for transaction in account['transactions']:
                if transaction['type'] == 'deposit':
                    cash_in += transaction['amount']
                elif transaction['type'] == 'withdraw':
                    cash_out += transaction['amount']
        print(f"Cash In: {cash_in}, Cash Out: {cash_out}")
#save account module
def save_accounts(self):
        save_data(self.data_file, self.accounts)
