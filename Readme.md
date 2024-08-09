

# Account Management System

## Library Modules

- `os`
- `json`
- `hashlib`
- `getpass`
- `datetime`

## Functions

### `hash_pin(pin: str) -> str`
Hashes a given PIN using SHA-256.

**Parameters:**
- `pin (str)`: The PIN to be hashed.

**Returns:**
- `str`: The hashed PIN.

### load_data(file_path: str) -> dict`
Loads JSON data from a file if it exists. Returns an empty dictionary if the file does not exist.

**Parameters:**
- `file_path (str)`: The path to the JSON file.

**Returns:**
- `dict`: The data loaded from the file.

### `save_data(file_path: str, data: dict) -> None`
Saves data to a JSON file.

**Parameters:**
- `file_path (str)`: The path to the JSON file.
- `data (dict)`: The data to be saved.

### `prompt_pin() -> str`
Securely prompts the user for their PIN.

**Returns:**
- `str`: The entered PIN.

## Classes

### `class Account`
Represents a user's account.

#### `__init__(self, username: str, pin: str, balance: float = 0, transactions: list = None, is_frozen: bool = False, transaction_limit: float = 1000)`
Initializes an account.

**Parameters:**
- `username (str)`: The username of the account.
- `pin (str)`: The PIN for the account.
- `balance (float)`: The initial balance (default is 0).
- `transactions (list)`: The list of transactions (default is None).
- `is_frozen (bool)`: Whether the account is frozen (default is False).
- `transaction_limit (float)`: The transaction limit (default is 1000).

#### `deposit(self, amount: float) -> None`
Deposits an amount into the account.

**Parameters:**
- `amount (float)`: The amount to be deposited.

#### `check_balance(self) -> None`
Prints the current balance.

#### `print_statement(self) -> None`
Prints the account statement (all transactions).

#### `transfer(self, amount: float, recipient: 'Account') -> None`
Transfers an amount to another account.

**Parameters:**
- `amount (float)`: The amount to be transferred.
- `recipient (Account)`: The recipient account.

#### `withdraw(self, amount: float) -> None`
Withdraws an amount from the account.

**Parameters:**
- `amount (float)`: The amount to be withdrawn.

#### `set_pin(self, new_pin: str) -> None`
Sets a new PIN for the account.

**Parameters:**
- `new_pin (str)`: The new PIN.

### `class Admin`
Represents the admin for managing user accounts.

#### `__init__(self, data_file: str = 'accounts.json')`
Initializes the admin with a data file.

**Parameters:**
- `data_file (str)`: The path to the data file (default is 'accounts.json').

#### `create_account(self, username: str, pin: str) -> None`
Creates a new account.

**Parameters:**
- `username (str)`: The username of the new account.
- `pin (str)`: The PIN for the new account.

#### `show_details(self, username: str) -> None`
Shows the details of a specific account.

**Parameters:**
- `username (str)`: The username of the account.

#### `show_transactions(self, username: str = None) -> None`
Shows transactions for a specific account or all accounts.

**Parameters:**
- `username (str)`: The username of the account (optional).

#### `delete_account(self, username: str) -> None`
Deletes an account.

**Parameters:**
- `username (str)`: The username of the account to be deleted.

#### `freeze_account(self, username: str) -> None`
Freezes an account.

**Parameters:**
- `username (str)`: The username of the account to be frozen.

#### `set_transaction_limit(self, username: str, limit: float) -> None`
Sets the transaction limit for an account.

**Parameters:**
- `username (str)`: The username of the account.
- `limit (float)`: The new transaction limit.

#### `generate_reports(self) -> None`
Generates reports on cash inflow and outflow.

#### `save_accounts(self) -> None`
Saves the accounts data to the file.

## CLI Interface Functions

### `user_menu(account: Account) -> None`
Displays the user menu and handles user interactions.

**Parameters:**
- `account (Account)`: The user's account.

### `admin_menu() -> None`
Displays the admin menu and handles admin interactions.

## Main

### `if __name__ == "__main__"`
Initializes the admin and presents the main menu for user login, admin login, or quitting the program.

