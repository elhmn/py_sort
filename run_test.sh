#!/bin/bash

deleteFolder()
{
	#delete temp folder

	if [ -e $temp_list_path ]
		then
			echo "$temp_list_path folder deleted OK"
			rm -rf $temp_list_path;
	fi
}

if [ $# -eq 0 ];then
	echo "Usage $0 <sort_algorithm_files>"
	exit -1
fi

for arg in $*
do
	if [ ! -e $arg ]
	then
		echo "$arg does'nt exist"
		exit -1
	fi
done

echo -e "\n[SORT ALGORITHMS TESTING PROGRAM]--------------------------------\n"

choice=0
order=none
temp_list_path=__listTemp__
temp_list_ord_path=__listOrdTemp__
list_file_name=list_
list_ord_file_name=list_ord_

while [ $choice -ne 1 ] && [ $choice -ne 2 ]
do
	echo -e "Choose your sorting order :"
	echo -e "1) Croissant\n2) Decroissant"
	read choice
done

case $choice in
	1) order=c; echo 'The test will run for "Croissant" order';;
	2) order=d; echo 'The test will run for "Decroissant" order';;
	else) order=none;;
esac

#Generation de fichier test

#Create temp folder

echo "[GENERATOR] file generation ..."

if [ ! -e $temp_list_path ]
	then
		echo "$temp_list_path folder created OK"
		mkdir -m 644 $temp_list_path;
fi

for i in $(seq 15)
do
	size=$(expr $RANDOM % 1000)
	max=$(expr $RANDOM % 1000)
	min=-$(expr $RANDOM % 1000)
	num=$i
	if [ $i -lt 10 ];then
		num="0$i"
	fi
	echo -e "$temp_list_path/$list_file_name$num : (size = $size, min = $min, max = $max) creation... -> \c"
	/usr/bin/time --format="real= %es" ./generator.py $size $min $max>$temp_list_path/$list_file_name$num

done

#Sort file

echo "[SORTING] sort files ..."
if [ ! -e $temp_list_ord_path ]
	then
		echo "$temp_list_ord_path folder created OK"
		mkdir -m 644 $temp_list_ord_path;
fi

for arg in $*
do
	echo "[SORTING] $arg test running..."
	a=0
	for e in $(ls $temp_list_path)
	do
		num=$a
		if [ $a -lt 10 ];then
			num="0$a"
		fi
		echo -e "$temp_list_path/$e :  sorting... -> \c"
		/usr/bin/time --format="real= %es" ./$arg $order $(cat $temp_list_path/$e)>$temp_list_ord_path/$arg\_$list_ord_file_name$num
		a=$(expr $a + 1)
	done
done

#now i test that everything was sorted

echo "[TEST] sort files ..."

if [ ! -e $temp_list_ord_path ]; then
	echo "$temp_list_ord_path does\'nt exist"
fi

for arg in $*
do
	echo "[TESTING] $arg test running..."
	for e in $(ls $temp_list_ord_path | grep $arg)
	do
		echo -e " ./$temp_list_ord_path/$e :  testing... -> \c"
		./tri_test.py $order $(cat ./$temp_list_ord_path/$e)
	done
done
