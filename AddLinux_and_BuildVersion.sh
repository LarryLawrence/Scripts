#!/bin/bash
for ((COUNT=1; COUNT<30+1; COUNT++))
do
	for FILE in $HOME/workspace/codes/testArea/classifiedStuff/$COUNT/*
	do
		filename="${FILE%%.*}"
	
			if [ $filename != $HOME/workspace/codes/testArea/classifiedStuff/$COUNT/build ] && [ $filename != $HOME/workspace/codes/testArea/classifiedStuff/$COUNT/RESULT ] && [ $filename != $HOME/workspace/codes/testArea/classifiedStuff/$COUNT/linux_n_build_ver ]
			then
		   	    python $HOME/workspace/codes/testArea/get_linux_version.py $FILE > $HOME/workspace/codes/testArea/classifiedStuff/$COUNT/linux_n_build_ver.txt
	 		    #echo $filename
			    #echo "-----------------------------------"> $HOME/workspace/codes/testArea/classifiedStuff/$COUNT/linux_n_build_ver.txt
			elif [ $filename == $HOME/workspace/codes/testArea/classifiedStuff/$COUNT/build ]
			then
			    python $HOME/workspace/codes/testArea/get_build_version.py $FILE >> $HOME/workspace/codes/testArea/classifiedStuff/$COUNT/linux_n_build_ver.txt
			fi
	done
done

