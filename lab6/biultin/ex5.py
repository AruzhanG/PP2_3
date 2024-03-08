def all_true_in_tuple(input_tuple):
    return all(element for element in input_tuple)

my_tuple = (True, True, False)
result = all_true_in_tuple(my_tuple)

print(result)        