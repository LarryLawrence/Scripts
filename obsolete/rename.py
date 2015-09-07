import os 
import shutil

path = 'E:\\33300~June25\\33100~33200'  
count=1
for file in os.listdir(path):
	if os.path.isfile('E:\\33300~June25\\33100~33200\\'+file):
		print file
	