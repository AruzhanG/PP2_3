import os
print('Exist: ',os.access("c.txt",os.F_OK))
file = 'c.txt'
location = "/Users/aruzhan/pp2_3/"
path = os.path.join(location, file)
os.remove(path)