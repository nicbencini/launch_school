"""
Building on the previous exercise, write a function that returns True or False based on whether or not an inventory item (an ID number) is available. 
As before, the function takes two arguments: an item ID and a list of transactions. The function should return True only if the sum of the quantity 
values of the item's transactions is greater than zero. Notice that there is a movement property in each transaction object. A movement value of 'out' 
will decrease the item's quantity.

You may (and should) use the transactions_for function from the previous exercise.

Program:
Input: 
- item_id
- transaction list
Output: Bool

Algorithm:
- Retrive transactions with given id using transactions_for
- For each transaction if "movement" value is 'in' then add it to a count
- If "movement" value is 'out' remove it from the count
- If final count value is greater than 0 then return True, otherwise return False
"""



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

def transactions_for(id, transaction_list):
    return [item for item in transaction_list if item["id"] == id]


def is_item_available(id, transaction_list):
    
    item_count = 0

    transaction_logs = transactions_for(id, transaction_list)

    for item in transaction_logs:
        if item["movement"] == 'in':
            item_count += item["quantity"]
        else:
            item_count -= item["quantity"]
    
    return item_count > 0

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True
