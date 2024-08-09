from account_module import Account
from utils import prompt_pin
from admin_module import Admin
"""   this class will be responsible for :
      user_menu : Responsible for showing the menu to the registered user and this can perform the all Accounts.py operation,
      admin_menu :Responsible for showing the Admin menu to the Admin and this can perform the all Admin.py operation ,
       
       
       """
       #User menu module
def user_menu(account, admin):
    while True:
        print("\nUser Menu")
        print("1. Deposit Amount")
        print("2. Check Balance")
        print("3. Print Statement")
        print("4. Transfer Amount")
        print("5. Withdraw Amount")
        print("6. Set/Change PIN")
        print("7. View Transaction History")
        print("8. Quit")

        choice = input("Choose an option: ")
        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            account.check_balance()
        elif choice == '3':
            account.print_statement()
        elif choice == '4':
            recipient_username = input("Enter recipient username: ")
            amount = float(input("Enter amount to transfer: "))
            recipient = admin.accounts.get(recipient_username)
            if recipient:
                account.transfer(amount, Account(**recipient))
                admin.save_accounts()
            else:
                print("Recipient account not found.")
        elif choice == '5':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
            admin.save_accounts()
        elif choice == '6':
            new_pin = prompt_pin()
            account.set_pin(new_pin)
            admin.save_accounts()
        elif choice == '7':
            account.print_statement()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")
#admin menu module
def admin_menu(admin):
    while True:
        print("\nAdmin Menu")
        print("1. Create Account")
        print("2. Show Account Details")
        print("3. Show Transactions")
        print("4. Delete Account")
        print("5. Freeze Account")
        print("6. Set Transaction Limit")
        print("7. Generate Reports")
        print("8. Quit")

        choice = input("Choose an option: ")
        if choice == '1':
            username = input("Enter username: ")
            pin = prompt_pin()
            admin.create_account(username, pin)
        elif choice == '2':
            username = input("Enter username: ")
            admin.show_details(username)
        elif choice == '3':
            username = input("Enter username (leave blank for all): ")
            admin.show_transactions(username if username else None)
        elif choice == '4':
            username = input("Enter username: ")
            admin.delete_account(username)
        elif choice == '5':
            username = input("Enter username: ")
            admin.freeze_account(username)
        elif choice == '6':
            username = input("Enter username: ")
            limit = float(input("Enter transaction limit: "))
            admin.set_transaction_limit(username, limit)
        elif choice == '7':
            admin.generate_reports()
        elif choice == '8':
            print("Exiting Admin Menu.")
            break
        else:
            print("Invalid choice. Please try again.")
