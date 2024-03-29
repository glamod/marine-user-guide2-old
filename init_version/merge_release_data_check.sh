#!/bin/bash
source ../setpaths.sh

sd_dck_list='/gws/smf/j04/c3s311a_lot2/code/marine_code/glamod-marine-config/marine-user-guide/v4/mug_v4_list.txt'
v4=$mug_data_directory/v4/level2
r1=$data_directory/r092019/ICOADS_R3.0.0T/level2
r2=$data_directory/release_2.0/ICOADS_R3.0.0T/level2

for sd in $(awk '{print $0}' $sd_dck_list)
do

	nheader_v4=$(ls $v4/$sd/header* 2> /dev/null | wc -l)
	nheader_r1=$(ls $r1/$sd/header* 2> /dev/null | wc -l)
	nheader_r2=$(ls $r2/$sd/header* 2> /dev/null | wc -l)
	echo "CHECKING $sd: $nheader_v4 $nheader_r1 $nheader_r2"
	num=$((nheader_r1 + nheader_r2))

if (( nheader_v4 != num ))
then
	echo "    ERROR $sd: numbers don't match"
fi
done
