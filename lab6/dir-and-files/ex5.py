l = ['mango','apple','banana']

with open('/Users/aruzhan/pp2_3/lab6/dir-and-files/myfile.txt', 'w+') as f:
	

	for items in l:
		f.write('%s\n' %items)
	
	print("File written successfully")

f.close()

