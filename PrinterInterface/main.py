import recordPrint
import register
import verifyContract
import viewDetails

print("\nWelcome to the printer interface\n")

choice = 0
while(choice != 5):

    print("\n\nEnter 1 to verify contract.")
    print("Enter 2 to view details of a contract")
    print("Enter 3 to register to a contract")
    print("Enter 4 to record print")
    print("Enter 5 to exit")

    choice = int(input("\nEnter your choice : "))

    if (choice == 1):
        verifyContract.verify_contract()
    elif (choice == 2):
        viewDetails.view_Details()
    elif (choice == 3):
        register.register()
    elif (choice == 4):
        recordPrint.record_print()
    elif (choice == 5):
        print("Exiting")
    else:
        print("Invalid option")