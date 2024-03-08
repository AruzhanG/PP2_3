with open(r'/Users/aruzhan/pp2_3/lab6/dir-and-files/myfile.txt', 'r') as fp:
	lines = len(fp.readlines())
	print('Total Number of lines:', lines)
