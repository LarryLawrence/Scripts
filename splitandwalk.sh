#!/bin/bash
COUNT=1
ALL=305	
while [ $COUNT != $ALL ]
do
    perl $HOME/workspace/codes/testArea/split_bootimg.pl $HOME/workspace/codes/testArea/classifiedStuff/$COUNT/boot.img
    mv boot.img-kernel ./classifiedStuff/$COUNT/
    let "COUNT=$COUNT+1"
    echo "HEYYYYYYYYYYYYYYYYYYYYIT'S $COUNT!!!!!!!!!!!"
done

    rm *ramdisk.gz

COUNTWALK=1
while [ $COUNTWALK != $ALL ]
do
    binwalk --dd='gzip:gz:gzip -d %e' $HOME/workspace/codes/testArea/classifiedStuff/$COUNTWALK/boot.img-kernel
    cp ./_boot*/* ./classifiedStuff/$COUNTWALK/
        
    rm -rf _boot*
#delete .gz files, .7z files, boot.img and boot.img-kernel
    rm ./classifiedStuff/$COUNTWALK/*.gz
    rm ./classifiedStuff/$COUNTWALK/*.7z
    rm ./classifiedStuff/$COUNTWALK/boot.img*
    let "COUNTWALK=$COUNTWALK+1"
done

for (( FOLDER=1; FOLDER < $COUNTWALK; FOLDER++ ))
#this sentense won't work: for FOLDER in {1..$COUNTWALK}
do
	ONETWO=0

	for FILE in $HOME/workspace/codes/testArea/classifiedStuff/$FOLDER/*
	do
	    let "ONETWO=$ONETWO+1"
	done
	if [ $ONETWO != 2 ]
	then
	    echo "it'sssssssssssssssssssssssssssss"+$ONETWO
	    rm -rf $HOME/workspace/codes/testArea/classifiedStuff/$FOLDER
	fi
done  
