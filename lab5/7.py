import re
input_text = input() 
print(''.join(x.capitalize() or '_' for x in input_text.split('_')))