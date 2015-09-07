#you should change 2 parameters :     1.filePath  2. for count in range()
import zipfile
import os 
import shutil


bootimgError = open('D:\\bootimgError.txt','w+')
propError = open('D:\\propError.txt','w+')
filePath = "F:\\33300~June25\\33300~33400\\"
for count in range(300,396+1): 
	try:
		f = zipfile.ZipFile(filePath + str(count) + '.zip','r')
	except:
		print str(count)+" has problem........"
	for file in f.namelist():	
		if file == 'boot.img':
			print str(count) + file	
			try:
				f.extract(file,filePath+"temp\\"+str(count)+"\\")
			except:
				bootimgError.write(str(count)+"\n")
				shutil.rmtree(filePath+"temp\\"+str(count)+"\\")
		if 'build.prop' in file:
			print file
			try:
				f.extract(file,filePath+"temp\\"+str(count)+"\\")
			except:
				propError.write(str(count)+"\n")
				shutil.rmtree(filePath+"temp\\"+str(count)+"\\")
							
	if os.path.exists(filePath+"temp\\"+str(count)+"\\system\\build.prop"):
		shutil.copyfile(filePath+"temp\\"+str(count)+"\\system\\build.prop", filePath+"temp\\"+str(count)+"\\"+"build.prop")
		shutil.rmtree(filePath+"temp\\"+str(count)+"\\system\\")