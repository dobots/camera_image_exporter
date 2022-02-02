#! /bin/bash
#


while getopts "o:t:" flag
do
	case "${flag}" in
		o) parameter_output=${OPTARG};;
		t) parameter_time=${OPTARG};;
	esac
done

if [ -z "$parameter_time" ]
then
	echo $parameter_time
else
	parameter_time=10
fi


ffmpeg -i "http://0.0.0.0:8080/stream?topic=/camera/image_raw" -t $parameter_time -f flv ../videos/MyOutput.mp4

