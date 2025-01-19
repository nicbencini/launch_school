nested_lists = [[1,1,1],
              [2,2,2],
              [3,3,3]]

flat_list = list((num
                  for sublist in nested_lists
                  for num in sublist))

print(flat_list)