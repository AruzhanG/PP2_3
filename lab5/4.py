import re
with open('/Users/aruzhan/pp2_3/lab5/row.txt', "r") as f:
    content = f.read()
    pattern = r'[A-Z]+[a-z]+'
    matching = re.findall(pattern, content)
    print(matching)