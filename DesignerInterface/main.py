import createContract
import creditAmount
import viewProducts

print("\nWelcome to the designer interface\n")

choice = 0
while(choice != 4):

    print("\n\nEnter 1 to create a new contract.")
    print("Enter 2 to credit an amount to the contract")
    print("Enter 3 to view printed product details")
    print("Enter 4 to exit")

    choice = int(input("\nEnter your choice : "))

    if (choice == 1):
        createContract.create_contract()
    elif (choice == 2):
        creditAmount.credit_amount()
    elif (choice == 3):
        viewProducts.view_products()
    elif (choice == 4):
        print("Exiting")
    else:
        print("Invalid option")