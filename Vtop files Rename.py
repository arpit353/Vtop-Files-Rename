import glob
import os

file_names = []
    
for i in glob.glob("*.*"):

	if(i == "rename.py"):
		os.remove(i)
	else :
	    last =  i.rfind('Material')
	    print i[last+9:]
	    
	    os.rename(i,i[last+9:])