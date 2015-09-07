__author__ = 'zhihuan'
import os
import sys
import shutil 

def help():
    print 'Usage:  get_build_version.py [build.prop FILE]\n'
    exit()

def main(argv):
    if len(argv)!=2:
        help()

    if os.path.exists(argv[1]):
	file = open(argv[1])
	while 1:
		line = file.readline()
		tag = line[:25]
		#print tag
		if( tag=="ro.build.version.release=" ):
			buildVer=line[21:]
			print line

		if not line:
			break

if __name__ == '__main__':
    main(sys.argv)
