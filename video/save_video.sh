#! /bin/bash
#

declare -i i=0

while getopts "o:t:" flag
do
	case $flag in
		o) 
			parameter_output=${OPTARG};;
			#echo "Name of output file $parameter_output"
		t) 
			
			parameter_time=${OPTARG}
			echo "Recording time $parameter_time seconds"
			;;
	esac
done

if [ -z "$parameter_time" ]
then	
	echo "No value given, Default Recording time 10"
	parameter_time=10
fi



if [ -z "$parameter_output" ]
then	
	echo "No Output file given, Default file name MyVideo.mp4"
	parameter_output="MyVideo.mp4"
fi


#while [[ ! -f ./saved/MyOutput_$i.mp4 && -z "$parameter_output" ]]
#do
#	((i++))	
#done	



#echo MyOutput_$i

ffmpeg -i "http://0.0.0.0:8080/stream?topic=/camera/image_raw" -t $parameter_time -f flv ../video/$parameter_output

