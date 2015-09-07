#author:zhihuan
import os 
import shutil
#
path = 'D:\\TEST\\unzipped' 
count=1
for file in os.listdir(path): 
	#if os.path.isdir(os.path.join(path,file))==True: 
#	if file.find('.')<0: 
	newname="a"+str(count)
	os.rename(os.path.join(path,file),os.path.join(path,newname)) 
	count=count+1
	print file,'ok' 

# print file.split('.')[-1] 

for newFolder in range(1,count):
	os.mkdir(os.path.join(path,str(newFolder)))

for copyCount in range(1,count): 
	if os.path.exists(path+"\\a"+str(copyCount)+"\\boot.img"):
		shutil.copyfile(path+"\\a"+str(copyCount)+"\\boot.img", path+"\\"+str(copyCount)+"\\boot.img")
	
for copyCount in range(1,count): 
	if os.path.exists(path+"\\a"+str(copyCount)+"\\system"+"\\build.prop"):
		shutil.copyfile(path+"\\a"+str(copyCount)+"\\system"+"\\build.prop", path+"\\"+str(copyCount)+"\\build.prop")