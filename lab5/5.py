import re
content=input()
pattern=r'a.*b$'
matching=re.findall(pattern,content)
print(matching)
