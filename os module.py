#python has different modules exaplmes:os module,shutil module,ect

import os
#os module in python provides function for interacting for operating system
cwd=os.getcwd()
#print(cwd)
#current working directory
#output:C:\Whitehatjr\CLASS 99



#os.chdir()is used to change the dicrectory
#os.chdir('../')
cwd=os.getcwd()
print(cwd)
os.chdir('C:\Whitehatjr\CLASS 99')
print(cwd)

#os.mkdir()is used to make a new dicrectory
#os.mkdir("sample")

#os.mkdirs()is used to create is used adicrectory recursively
os.makedirs("folderA/B/C/D")
