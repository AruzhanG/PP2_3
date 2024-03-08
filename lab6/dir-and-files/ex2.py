import os 
print('Exist: ',os.access("/Users//aruzhan//pp2_3",os.F_OK))
print('Readable: ',os.access("/Users//aruzhan//pp2_3",os.R_OK))
print('Writable: ',os.access("/Users//aruzhan//pp2_3",os.W_OK))
print('Executable ',os.access("/Users//aruzhan//pp2_3",os.X_OK))

