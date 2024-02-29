import re
with open("row.txt", "r") as f:
    content = f.read()
    pattern = r'[A-Z]+[a-z]+'
    matching = re.findall(pattern, content)
    print(matching)