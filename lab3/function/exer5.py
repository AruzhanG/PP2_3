from itertools import permutations

def print_permutations(input_str):
  
    all_permutations = permutations(input_str)

   
    for perm in all_permutations:
        print("".join(perm))


user_input = input("Enter a string: ")
print_permutations(user_input)