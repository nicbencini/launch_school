
test_list = [1,2,3,4,5,6,7,8,9,10]



def sum_pair(input_list):

    if len(input_list) == 1:
        return input_list

    list_1 = input_list[::len(input_list)//2]
    list_2 = input_list[len(input_list)//2::]

    list_1 = sum_pair(list_1)
    list_2 = sum_pair(list_2)

    return input_list[0]


print(sum_pair(test_list))
