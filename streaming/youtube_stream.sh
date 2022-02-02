#! /bin/bash
#
# s indicates the source of the videostream default: http://0.0.0.0:8080/stream?topic=/camera/image_raw
#
#
#
#Sourcing stream key value
MAIN_SCRIPT_DIR=$(dirname "${BASH_SOURCE[0]}")
echo $MAIN_SCRIPT_DIR
#cd MAIN_SCRIPT_DIR
. key.conf
echo $KEY

while getops i:k: flag
do
	case "${flag}" in
		s) input=$(OPTARG);;
		k) key=$(OPTARG);;
	esac
done

if [ -n $input ]
then
	input = http://0.0.0.0:8080/stream?topic=/camera/image_raw
fi

ffmpeg 	\
	-re -f mjpeg\
        -i "http://0.0.0.0:8080/stream?topic=/camera/image_raw" -f lavfi -i anullsrc -c:v libx264\
        -g 60 -c:a aac -ar 44100 -ac 2\
        -f flv "rtmp://a.rtmp.youtube.com/live2/${KEY}"

