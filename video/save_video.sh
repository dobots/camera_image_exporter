#! /bin/bash
#

declare -i i=0

while getopts "o:t:" flag
do
         case $flag in
                 o)
                         parameter_output=${OPTARG}
			 if [[ ! $parameter_output == .mp4 ]] && [ -z "parameter_output" ]
  			 then
          			parameter_output="$parameter_output.mp4"

  			fi
			if [ -f ./saved_videos/$parameter_output.mp4 ]
 			then
 				echo "The filename $parameter_output is already in use, choose a different name"
 				exit 0
 			fi

			;;
                       #echo "Name of output file $parameter_output"
                 t)
 
                         parameter_time=${OPTARG}
                         echo "Recording time $parameter_time seconds"
                         ;;
         esac
done

#if [[ ! $parameter_output == .mp4 ]] && [ -z "parameter_output" ]
#then
#	parameter_output="$parameter_output.mp4"
#
#fi



if [ -f ./saved_videos/$parameter_output ]
then
	echo "The filename $parameter_output is already in use, choose a different name"
	exit 0
fi

echo "$parameter_output"
if [ -z "$parameter_output" ]
then
while [ -f ./saved_videos/MyVideo$i.mp4 ]
do
	((i++)) 
done
echo "No output file given, your video will be saved as MyVideo$i.mp4"
fi

if [ -z "$parameter_time" ]
then
        echo "No value given, Default Recording time 10"
         parameter_time=10
fi


ffmpeg -i "http://0.0.0.0:8080/stream?topic=/camera/image_raw" -t $parameter_time -f flv ../video/$parameter_ou    tput

