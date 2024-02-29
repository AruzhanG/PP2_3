import re
input=input()
pattern = r'(?=[A-Z])'
result = re.split(pattern, input)
print(result)