import createContract
import creditAmount
import viewProducts
import approveOrFail

print("\nWelcome to the designer interface\n")

choice = 0
while(choice != 6):

    print("\n\nEnter 1 to create a printer friendly contract.")
    print("Enter 2 to create a designer friendly contract")
    print("Enter 3 to credit an amount to the contract")
    print("Enter 4 to view printed product details")
    print("Enter 5 to approve/fail product")
    print("Enter 6 to exit")

    choice = int(input("\nEnter your choice : "))

    if (choice == 1):
        createContract.printer_friendly_contract()
    elif (choice == 2):
        createContract.designer_friendly_contract()
    elif (choice == 3):
        creditAmount.credit_amount()
    elif (choice == 4):
        viewProducts.view_products()
    elif (choice == 5):
        approveOrFail.approve_or_fail()
    elif (choice == 6):
        print("Exiting")
    else:
        print("Invalid option")