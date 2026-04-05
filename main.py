#amount
amount = input("Enter amount: ")

#transaction
transaction_type = input("Is this income or expense?")

#category
category = input("Enter category (food, rent, etc.): ")

#date
date = input("Enter Date (YYYY-MM-DD): ")

#prints everything
print("Transaction:", amount, transaction_type, category, date)


#transactions list
#create an empty list to store the transactions
transactions = []

#add transactions to list
transactions.append({
    "amount": amount,
    "type": transaction_type,
    "category": category,
    "date": date
})

#prints all transactions
print("All Transactions:", transactions)
