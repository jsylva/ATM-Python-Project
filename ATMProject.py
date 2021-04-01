# This program simulates a simple ATM.
# @author Jacob Sylva 

# Initial setup
MAX_ATTEMPTS = 3
PIN = "12ab"
balance = 1500

# Get the customer's pin
userPin = ""
numAttempts = 0
while (numAttempts < MAX_ATTEMPTS and PIN != userPin):
    userPin = input("Enter PIN: ")
    numAttempts += 1

# If successful PIN entry proceed with menu processing 
# otherwise tell customer to reset PIN
if (userPin == PIN):
    # Continue to present and process customer choices
    # until the customer chooses to exit.
    menuChoice = "0"

    while (menuChoice != "4"):
        # Display menu and get the customer's choice
        print('\n(1) Withdraw money')
        print('(2) Deposit money')
        print('(3) Show balance')
        print('(4) Exit')
        menuChoice = input('Your choice: ')
        # Process the choice
        if (menuChoice == "1"):
            withdrawAmmount = float(input("Withdraw ammount: $"))
            balance -= withdrawAmmount
        elif (menuChoice == "2"):
            depositMoney = float(input('Deposit ammount: $'))
            balance += depositMoney
        elif (menuChoice == "3"):
            print(f'Balance: ${balance:,.2f} ')
        elif (menuChoice == "4"):
            print('Have a good day. ')
        else:
            print('Invalid choice')
        print()
else: 
    print('Maximum attempts reached. You will need to reset your PIN.')
