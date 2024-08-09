from admin_module import Admin
from cli import user_menu, admin_menu
from utils import prompt_pin, hash_pin
from account_module import Account
"""
    this class will be responsible for :
      Showing the complete architecture of the system to the user and admin as well.
      
       
       
      """
if __name__ == "__main__": #indicate the main class
    admin = Admin()
    while True:
        print("\nMain Menu")
        print("1. User Login")
        print("2. Admin Login")
        print("3. Quit")

        choice = input("Choose an option: ")
        if choice == '1':
            username = input("Enter username: ")
            pin = prompt_pin()
            account_data = admin.accounts.get(username)
            if account_data and account_data['pin'] == hash_pin(pin):
                user_menu(Account(**account_data), admin)
            else:
                print("Invalid credentials.")
        elif choice == '2':
            admin_menu(admin)
        elif choice == '3':
            print("Exiting Main Menu.")
            break
        else:
            print("Invalid choice. Please try again.")
