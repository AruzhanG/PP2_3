import re
with open('/Users/aruzhan/pp2_3/lab5/row.txt', "r") as f:
    content = f.read()
    pattern = "ab+"
    if re.search(pattern, content):
        matching=re.findall(pattern,content)
        print(matching)