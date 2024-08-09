import json
import os
import hashlib
import getpass
"""
    this class will be responsible for :
      hash_pin : Responsible for encrypt the pin in hash,
      load_data : This module load all the data to json with read only mode,
      save_data: this module write the data of accounts and transaction history,
       prompt_pin : by using the getpass it does not shows the pin on cli,
       
      """           
      # hash pin module 
def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()
#load data module
def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return {}
#save data module
def save_data(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
#prompt pin module
def prompt_pin():
    return getpass.getpass("Enter PIN: ")
