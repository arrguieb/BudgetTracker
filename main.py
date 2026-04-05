transactions = []

while True:
        amount = input("Enter amount: ")
        transaction_type = input("Is this income or expense?")
        category = input("Enter category (food, rent, etc.): ")
        date = input("Enter Date (YYYY-MM-DD): ")
#add transactions to list
        transactions.append({
            "amount": amount,
            "type": transaction_type,
            "category": category,
            "date": date
        })

        print("Transaction added")

        #asks user if they want to add another transaction
        cont = input("Add another? (y/n)")
        if cont.lower() != "y":
                break

#prints all transactions
print("All Transactions:", transactions)

