import re
with open("row.txt", "r") as f:
     content = f.read()
     pattern = "ab+"
     if re.search(pattern, content):
         matching=re.findall(pattern,content)
         print(matching)
      