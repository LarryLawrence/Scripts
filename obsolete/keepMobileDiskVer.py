#author:zhihuan
import os 
import shutil
#
path = 'E:\\33300~June25\\33100~33200' 
count=1
#first we have to rename the folders into some regular name so we can TRAVERSE the folders in order
for file in os.listdir(path): 
	if os.path.isdir('E:\\33300~June25\\33100~33200\\'+file):
	#if os.path.isdir(os.path.join(path,file))==True: 
#	if file.find('.')<0: 
		newname="a"+str(count)
#rename the folders into a1,a2,a3..
		os.rename(os.path.join(path,file),os.path.join(path,newname)) 
		count=count+1
		print file,'ok' 

# print file.split('.')[-1] 

#make new folders whose name are 1,2...
for newFolder in range(1,count):
	os.mkdir(os.path.join(path,str(newFolder)))
#copy boot.img and build.prop from a1,a2,..to 1,2...
for copyCount in range(1,count): 
	if os.path.exists(path+"\\a"+str(copyCount)+"\\boot.img"):
		shutil.copyfile(path+"\\a"+str(copyCount)+"\\boot.img", path+"\\"+str(copyCount)+"\\boot.img")
	
for copyCount in range(1,count): 
	if os.path.exists(path+"\\a"+str(copyCount)+"\\system"+"\\build.prop"):
		shutil.copyfile(path+"\\a"+str(copyCount)+"\\system"+"\\build.prop", path+"\\"+str(copyCount)+"\\build.prop")