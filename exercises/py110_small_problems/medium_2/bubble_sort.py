"""
Bubble Sort is one of the simplest sorting algorithms available. It is not an efficient algorithm, so developers rarely use it in real code. However, it is an excellent 
exercise for student developers. In this exercise, you will write a function that sorts a list using the bubble sort algorithm.

A bubble sort works by making multiple passes (iterations) through a list. On each pass, the two values of each pair of consecutive elements are compared. 
If the first value is greater than the second, the two elements are swapped. 
This process is repeated until a complete pass is made without performing any swaps. At that point, the list is completely sorted.

We can stop iterating the first time we make a pass through the list without making any swaps since that means the entire list is sorted.

For further information -- including pseudo-code that demonstrates the algorithm, as well as a minor optimization technique -- see the Bubble Sort Wikipedia page.

Write a function that takes a list as an argument and sorts that list using the bubble sort algorithm described above. The sorting should be done "in-place" -- that is, 
the function should mutate the list. You may assume that the list contains at least two elements.

Problem:
    -Create an algortihm which sorts a list in ascending order using bubble sorting

Rules:
    # Input list can contain integers and strings
    # Input list will have at least 2 items
    # The function should not mutate the list
    # Function will stop running once list has been sorted

Examples:
    lst1 = [5, 3]
    bubble_sort(lst1)
    print(lst1 == [3, 5])                   # True

    lst2 = [6, 2, 7, 1, 4]
    bubble_sort(lst2)
    print(lst2 == [1, 2, 4, 6, 7])          # True

    lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
    bubble_sort(lst3)

    expected = ["Alice", "Bonnie", "Kim", "Pete",
                "Rachel", "Sue", "Tyler"]
    print(lst3 == expected)                 # True

Data: 
    Input: List of items to sort
    Output: Sorted list in ascending order

Algorithm:
    - Reference list into function
    - Iterate over list using while loop:
    - For each item in list, check if item is greater than next item
    - If so swap items in the list by mutating it
    - break list if no changes occur

Pseduo Code for main function:

    START

    # Given a collection of itegers called "input_list"

    WHILE True:

        "previous_list" = shallow copy of "input_list"

        SWAP_ITEMS("input_list") # mutates "input_list"

        IF "previous_list" == "input_list"
            BREAK
        
    END

Psudo Code for SWAP_ITEMS:

    START

    # Given a collection of integers passed by reference called "number_list"

    FOR "number" IN "number_list"
        IF "number" < "next_number"
            swap numbers by mutating list

    END

"""

def swap_items(number_list):
    for i in range(len(number_list)):
        if i + 1 < len(number_list):
            if number_list[i] > number_list[i + 1]:
                number_list[i], number_list[i + 1] = number_list[i + 1], number_list[i]

def bubble_sort(input_list):

    while True:
        previous_list = input_list.copy()

        swap_items(input_list)

        if input_list == previous_list:
            break

test_lst = [5,4,3,2,1]

swap_items(test_lst)
swap_items(test_lst)

print(test_lst)

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True

