"""
Calculate the product of all numbers in a list using the reduce function.
"""

def reduce(callback, iter, start):

    result = start
    for item in iter:
        result = callback(result,item)
    
    return result


input_list = [1,1,2,3]

print(reduce(lambda x,y: x*y, input_list[1::],input_list[0]))