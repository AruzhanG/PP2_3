import re
with open("row.txt", "r") as f:
    content = input()
    pattern = r'[a-z]+_[a-z]+'
    matching = re.findall(pattern, content)
    print(matching)