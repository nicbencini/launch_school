

def inverse(input_number_list):

    output_list = []
    
    for number in input_number_list:
        try:
            result = 1/number
        except (ValueError, ZeroDivisionError, TypeError):
            result = 'Not Valid'
        finally:
            output_list.append(result)
    
    return output_list

number_list = [1,4,'w',4,'e',0,0,4,4,4]

print(inverse(number_list))