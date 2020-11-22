import os
DIR_PATH='train201701'
files=os.listdir(DIR_PATH)

for filename in files:
	name,suffix=os.path.splitext(filename)
	rename='0000000'
	rename=rename+name[12:17]+'.jpg';
	old_name=os.path.join(DIR_PATH,filename)
	new_name=os.path.join(DIR_PATH,rename)
	os.rename(old_name,new_name)