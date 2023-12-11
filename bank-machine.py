# Programmer : Alexander Walker
# Description : This program ask the user to enter in a list of withdrawals and deposits, it then shows a summary at the end.

#Counters for the summary and for the amount of times the program will ask the user the question of withdrawals or deposits.
count = 1
total_deposit = 0
total_withdrawn = 0

#User enters in there starting balance here.
starting_balance = int(input("What is your starting balance? "))

#They enter in how many transactions there going to make here.
num_of_transactions = int(input("How many transactions are there? "))


#While count is < than num_of_transactions, the program will repeat the following.
while (count <= num_of_transactions):
    #The user is asked if the first transaction is a withdrawal or deposit
    tran1 = input(f"\nIs transaction {count} a deposit or withdrawal? [D/W] ")
    
    #If they put D, for deposit, the following will occur.
    if (tran1 == "D"):
        deposit_amount = int(input("How much is being deposited? "))
        
        #Adds to the total amount of deposits, and adds a point to the transaction counter.
        total_deposit = total_deposit + deposit_amount
        count += 1
    
    #If they put W, for withdrawal, the following will occur.
    elif (tran1 == "W"):
        withdrawn_amount = int(input("How much is being withdrawn? "))
        
        #Adds to the total amount of deposits, and adds a point to the transaction counter.
        total_withdrawn = total_withdrawn + withdrawn_amount
        count += 1
        
    #If tran1 does not = W, or D for withdrawal or deposit then the following will occur.
    else:
        #While tran1 does not = W, or D, it will give an error message and prompt the user to try again.
        while (tran1 != "W") and (tran1 != "D"):
            print("Invalid choice! Try again.")
            tran1 = input(f"\nIs transaction {count} a deposit or withdrawal? [D/W] ")
            
            if (tran1 == "D"):
                deposit_amount = int(input("How much is being deposited? "))
                total_deposit = total_deposit + deposit_amount
                count += 1
                
            elif (tran1 == "W"):
                withdrawn_amount = int(input("How much is being withdrawn? "))
                total_withdrawn = total_withdrawn + withdrawn_amount
                count += 1


#=-=-=-=-=-=-=-(SUMMARY)-=-=-=-=-=-=-=-=
                
#Gives a summary of all the transactions made, deposits, and withdrawals, as well as giving the new balance.

print("\nSUMMARY")
print("-=-=-=-")
print(f"Starting Balance: ${starting_balance:,.2f}")
print(f"Deposits: ${total_deposit:,.2f}")
print(f"Withdrawals: ${total_withdrawn:,.2f}")

new_balance = starting_balance + total_deposit - total_withdrawn

print(f"New balance: ${new_balance:,.2f}")

            
            

            
            
