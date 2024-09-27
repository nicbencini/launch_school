"""
Write a function that takes two arguments, an inventory item ID and a list of transactions, and returns a list containing only the transactions for the specified inventory item.

Program:
Input: 
- Item Id as integer
- Dictionary with list of transactions

Output:
- List of dictionaries for item ID

Algorithm
- cycle through vales for id in transaction dictionaries
- If the value is equal to the given ID append to output list
- Return output_list

"""

def transactions_for(id, transaction_list):
    return [item for item in transaction_list if item["id"] == id]

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True


