import re
input_text =input()
pattern = r'([A-Z])'
replaced_text = re.sub(pattern, r' \1', input_text)
print(replaced_text)
