import designHelpers as dh 
from web3 import Web3
import os

print("\nWelcome to the manage design interface\n")

provider = Web3.IPCProvider(os.path.join(os.path.dirname(__file__), '../DesignNode/geth.ipc'))
w3 = Web3(provider)
choice = 0
while(choice != 5):

    print("\n\nEnter 1 to upload a new design.")
    print("Enter 2 to get no of design files stored")
    print("Enter 3 to view design file details")
    print("Enter 4 to update the design")
    print("Enter 5 to exit")

    choice = int(input("\nEnter your choice : "))

    if (choice == 1):
        dh.upload_design(w3)
    elif (choice == 2):
        dh.get_files_length(w3)
    elif (choice == 3):
        dh.get_design(w3)
    elif (choice == 4):
        dh.update_design(w3)
    elif (choice == 5):
        print("Exiting")
    else:
        print("Invalid option")