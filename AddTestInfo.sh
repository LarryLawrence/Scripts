#!/bin/bash
for (( COUNT=1; COUNT < 304; COUNT++ ))
do
	for FILE in $HOME/workspace/codes/testArea/classifiedStuff/$COUNT/*
	do
	#FILE="example.tar.gz"
	#FILE=$HOME/workspace/codes/testArea/classifiedStuff/$COUNT/build.prop 
		#echo "${FILE%%.*}"
		filename="${FILE%%.*}"
	
		if [ $filename != $HOME/workspace/codes/testArea/classifiedStuff/$COUNT/build ] && [ $filename != $HOME/workspace/codes/testArea/classifiedStuff/$COUNT/RESULT ]
		then
	   	    $HOME/workspace/codes/testArea/test $FILE > $HOME/workspace/codes/testArea/classifiedStuff/$COUNT/RESULT.TXT
 		#echo $filename
		fi
	done
done
