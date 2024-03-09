import re
with open( '/Users/aruzhan/pp2_3/lab5/row.txt', "r") as f:
    content = f.read()
    pattern1 = "abb"
    pattern2 = "abbb"
    if re.search(pattern1, content) or re.search(pattern2,content):
         matching1=re.findall(pattern1,content)
         matching2=re.findall(pattern2,content)
         print(matching1,matching2)

