test_list = [None, 1, None, 2, None, 3]

cleaned_list = filter(lambda x: x is not None, test_list)

print(list(cleaned_list))