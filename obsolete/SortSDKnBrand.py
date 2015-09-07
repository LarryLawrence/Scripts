import os
import shutil 
#classify the sdk version				
for i in range(1,100+1):
	if os.path.exists("D:\\TEST\\classifiedStuff\\"+str(i)):
		file = open("D:\\TEST\\classifiedStuff\\" + str(i) + "\\build.prop")
		while 1:
			line = file.readline()
			if not line:
				break
			tag = line[:-3]
			if( tag=="ro.build.version.sdk=" ):
				sdkVerNum=line[21:]
				print sdkVerNum
				if int(sdkVerNum) >= 14:
#please delete the folders in D:\TEST\ICSorNot\14Higher before do this ,otherwise there will be errors
					if not os.path.exists("D:\\TEST\\ICSorNot\\14Higher\\"+str(i)+"\\"):
						shutil.copytree("D:\\TEST\\classifiedStuff\\"+str(i)+"\\",  "D:\\TEST\\ICSorNot\\14Higher\\"+str(i)+"\\")				
				elif int(sdkVerNum) < 14:
					if not os.path.exists("D:\\TEST\\ICSorNot\\14Higher\\"+str(i)+"\\"):	
						shutil.copytree("D:\\TEST\\classifiedStuff\\"+str(i)+"\\",  "D:\\TEST\\ICSorNot\\14Lower\\"+str(i)+"\\")										

#classify the brand
for i in range(1,100+1):
	if os.path.exists("D:\\TEST\\ICSorNot\\14Higher\\"+str(i)):
		file = open("D:\\TEST\\ICSorNot\\14Higher\\" + str(i) + "\\build.prop")
		while 1:
			line = file.readline()
			if not line:
				break
			tag = line[:17]
			if( tag=="ro.product.brand=" ):
					brand=line[17:-1]
					#print brand
					if not os.path.exists("D:\\TEST\\ICSorNot\\14Higher\\"+brand):
						os.mkdir("D:\\TEST\\ICSorNot\\14Higher\\"+brand)
						if not os.path.exists("D:\\TEST\\ICSorNot\\14Higher\\"+brand+"\\"+str(i)):
							shutil.copytree("D:\\TEST\\ICSorNot\\14Higher\\"+str(i)+"\\",  "D:\\TEST\\ICSorNot\\14Higher\\"+brand+"\\"+str(i))				
					#shutil.rmtree("D:\\TEST\\ICSorNot\\14Higher\\"+str(i)+"\\")
					

