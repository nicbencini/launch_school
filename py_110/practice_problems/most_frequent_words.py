# Pete is baking cakes and needs help calculating how many he can make with his recipes and available ingredients.
# Write a function cakes() that takes two dictionaries: the recipe and the available ingredients. 
# 
# Return the maximum number of cakes Pete can bake.

# Rules:
# - Ingredients not present in the objects can be considered as 0.

"""
Problem:
    Create a function that can help calcualte how many cakes can be baked.
    First input is the recepie and the second input is the ingredients.

Rules:
    - Ingerdients not present in the objects can be considered as 0.
    - There may be more ingredients then the recepie needs
    - There may be less ingredients then the recepie needs
    - Ingredient dictionary can be empty

Examples:
    print(cakes({"flour":500, "sugar":200, "eggs":1},{"flour":1200, "sugar":1200, "eggs":5, "milk":200}) == 2)

Algorithm:
    - create cake_counter variable list
    - cycle through the items of the recepie dictionary
        - get the number of requried items
        - check if item exists in available ingredients
            - if not break and return  0
        - if item exists check how many cakes can be made with that item
        - append answer to cake_counter variable list
    - get the minimum value from item count varible list and return


"""




def cakes(ingredients, available):
    cake_counter = []

    for item in ingredients.items():

        ingredient = item[0]
        ingredient_count = item[1]

        if ingredient not in available:
            return 0
        
        available_count = available[ingredient]

        if ingredient_count != 0:
            result = available_count//ingredient_count

            cake_counter.append(result)
    
    return min(cake_counter)

 

# must return 2
print(cakes({"flour":500, "sugar":200, "eggs":1},{"flour":1200, "sugar":1200, "eggs":5, "milk":200}) == 2)

# must return 11
print(cakes({"cream":200, "flour":300, "sugar":150, "milk":100, "oil":100},{"sugar":1700, "flour":20000,
"milk":20000, "oil":30000, "cream":5000}) == 11)

# must return 0
print(cakes({"apples":3, "flour":300, "sugar":150, "milk":100, "oil":100},{"sugar":500, "flour":2000,
"milk":2000}) == 0)

# must return 0
print(cakes({"apples":3, "flour":00, "sugar":150, "milk":100, "oil":100},{"sugar":500, "flour":2000,
"milk":2000, "apples":15, "oil":20}) == 0)

# must return 0
print(cakes({"eggs":4, "flour":400},{}) == 0)

# must return 1
print(cakes({"cream":1, "flour":3, "sugar":1, "milk":1, "oil":1, "eggs":1},{"sugar":1, "eggs":1, "flour":3,"cream":1, "oil":1, "milk":1}) == 1)