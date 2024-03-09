import re

def find_sequences(input_string):
    pattern = r'[a-z]+_[a-z]+'
    matching_sequences = re.findall(pattern, input_string)
    return matching_sequences


example_string = "abc_def ghi_jkl_mno pqr"
result = find_sequences(example_string)


print(f"Sequences of lowercase letters joined with an underscore: {result}")
