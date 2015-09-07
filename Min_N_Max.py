#this file will classify min, max, linuxVer, buildVer, brand and board value in a already 'handled' folder like 'E:\\33300~June25\\33100~33200\\'
#if the min or max value does not exist (like error occurred when running 'test'),that list will not be added into the text file

#author zhihuan
import os 
import shutil

filePath = 'E:\\33300~June25\\33100~33200\\handled\\'  
fmin= open('D:\\min.txt','w')
fmax= open('D:\\max.txt','w')  
linuxVer= open('D:\\linuxVer.txt','w')
buildVer= open('D:\\buildVer.txt','w')
brand= open('D:\\brand.txt','w')
board= open('D:\\board.txt','w')

#for folder in os.listdir(path):
#using 'path.isdir' you will not need to judge existing or not	
for count in range(1,100+1):
	if os.path.isdir(filePath + str(count)):
		print count
		fileResult = open(filePath + str(count) + '\\RESULT.TXT')
		fileVer = open(filePath + str(count) + '\\linux_n_build_ver.txt')
		fileProp = open(filePath + str(count) + '\\build.prop')
		lineResult = fileResult.readline();

		lineProp = fileProp.readline();
		while 1:
			if lineResult!='':
				arr=lineResult.split(' ');		
				min = arr[2]
				max = arr[4]			
			#judging if there was an offset(or error)
			if min.isdigit():
				fmin.write(min+'\n')	
				#min = 'alpha'
				#only when there's an offset , write the linuxVer and buildVer
				for i in range(1,4+1):	
					ver =  fileVer.readline()
					if i == 2:
						if ver[26:] != '':
							linuxVer.write(ver[26:])
						else:
							linuxVer.write('null\n')
					if i == 4:
						if ver[25:] !='':
							buildVer.write(ver[25:])
						else:
							buildVer.write('null\n')
				print lineProp
				

				boardCount=0
				brandCount=0	
				for j in range(1,1000):
					lineProp= fileProp.readline()
					if "ro.product.board" in lineProp:
						board.write(lineProp)					
						boardCount=boardCount+1
						
					if "ro.product.brand" in lineProp:
						brand.write(lineProp)
						brandCount=brandCount+1	
						
				if boardCount == 0:
					board.write('null\n')
				if brandCount == 0:
					brand.write('null\n')				

					
				# brandCount=0					
				# for i in range(1,1000):
					# lineProp= fileProp.readline()
					# if "ro.product.brand" in lineProp:
						# brand.write(lineProp)
						# brandCount=brandCount+1	
						# break
				# if brandCount == 0:
					# brand.write('null\n')
					
			if max[:-1].isdigit():
				fmax.write(max[:-1]+'\n')
				

			break