import re

input_text = input()
pattern = r'[ ,.]'
replaced_text = re.sub(pattern, ':', input_text)
print(replaced_text)