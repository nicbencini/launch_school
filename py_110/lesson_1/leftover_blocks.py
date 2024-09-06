
"""
Problem

Inputs: integer for number of valid blocks
Outputs: [integer for number of blocks remaining

Explicit Rules:
- Top layer is a single block
- Block in upper layer must be supported by four blocks
- Block in lower layer can support more than one block in upper layer
- There cannot be any gaps between blocks

Implicit rules:
- Layer number correlates with blocks in a layer:
- The number of blocks in a layer is layer number * layer number.

Clarfiying Questions:
- What is a cube and how is it defined.
- How is a collection of blocks defined? 
- Define what it means to be supported. Does this mean that blocks need to be in row below?

Test Cases:

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True

Data Structures:

['x'],                                              1
['x', 'x', 'x', 'x'],                               4
['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],      9

Algorithm

1. Create local variable to store integer of available blocks
2. Use while loop to cycle through incrementally increasing integer starting from 0 and calculate it square
3. Incramentally add square values until sum is greater than value for available blocks
4. Store the value of squares from the previous iteration before it increased past the sum of available blocks
5. Use modulus function to calculate the remaining amount of blocks and return this value


"""

def calculate_leftover_blocks(available_blocks):

    if available_blocks == 0:
        return 0
    
    used_blocks = 0
    row_counter = 1

    while True:
        
        if used_blocks + row_counter**2 > available_blocks:
            break

        used_blocks += row_counter**2

        row_counter += 1
    
    print(used_blocks)
    print(available_blocks%used_blocks)


    return  available_blocks%used_blocks

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True