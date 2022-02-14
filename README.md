# Camera Image Exporter
A robot which can track an object or Robot in Gazebo, and stream the video via Youtube, (Or Twitch). Or save the video recording.

To Do:
- Make camera functional in GzWeb
- Streamline launch files and nodes
- Include Twitch Stream

## 1. HOW TO USE:

### 1.0.0 Optional: Using the Simcloud Docker image
You may use the Simcloud Docker image from DoBots.
Simcloud Docker Image (https://github.com/dobots/simcloud)
This file is also available in this repository in the docker directory.

""If you are not familiar with Docker, it is recommended to use the Simcloud tutorial.""

       

### 1.0 Clone the repository and build package
Navigate to your catkin workspace, if you do not have one, [create one](http://wiki.ros.org/catkin/Tutorials/create_a_workspace).

Clone this repository and [build the catkin package](https://catkin-tools.readthedocs.io/en/latest/verbs/catkin_build.html)


In your catkin workspace, navigate to the src file and clone the repo:

```
cd src
git clone https://github.com/dobots/camera_image_exporter.git
cd ..
catkin_make
```

 

### 1.1.1  Launching the environment in Simcloud
After cloning the repository.
Navigate to the repository
```
cd camera_image_exporter
```

This system can be run on any world, but for this example we will be using the Simple Shape environment from the Simcloud repository.
```
roslaunch environments simple_shapes.launch
```
![gazebo_shapes](https://user-images.githubusercontent.com/27964546/151209141-92733f6a-b388-4e67-8164-b6979542822a.png)

### Alternative: Launching Environment without Simcloud
If you do not want to use the simcloud environment, you may use the gazebo empty world.
```
roslaunch gazebo_ros empty_world.launch
```
If you do use the gazebo empty_word:
Insert a box into the world, by clicking the box object in Gazebo and inserting it into the world.
![Square_Marked_red](https://user-images.githubusercontent.com/27964546/153565973-8d534516-7dc9-43c2-8866-7846f0763625.png)

### 1.1 Launch the camera model
Here we will launch the camera model. The camera model is a simple "Robot" which outputs a video stream as a topic.
```
roslaunch camera_image_exporter spawn_model.launch
```
The camera is launched but is not tracking any object. To track an object we will use the pos.py node.
The pos.py node can be located in the ""scripts"" directory of this repository.
```
camera_image_exporter
|---   scripts
       |
       |---   pos.py
```
To use this node you must give it an object to track. Open Gazebo and give it a model to track from the model list.
Marked in the red square below:
![gazebo_models](https://user-images.githubusercontent.com/27964546/151209328-1fc4e32d-fb42-451a-a2a9-fed1ca7b86b3.png)

To run the node pos.py, you must give at an object to follow. Thus the structure would be:

rosrun camera_image_exporter pos.py [object_name]

So for this example we will use unit_box

```
rosrun camera_image_exporter pos.py unit_box
```

If run correctly the camera is now linked to that object, and will also update its position if the object is moved.
You may test this by manually moving the object in Gazebo, for example by changing the x values (displayed bellow):
![locked_pic](https://user-images.githubusercontent.com/27964546/153851804-4c9886df-71b8-4ae8-8a95-0865b7791b9d.png)


### 1.2 Viewing the video stream
The camera robot locks onto an object and streams the video via a [Ros Topic](http://wiki.ros.org/Topics). And thus can be interacted with. To see if the camera robot has been launched succesfully, open a terminal and execute the following commands:
```
rostopic list
```
If the camera has been launched succesffuly, the topic
```
/camera/image_raw"
```
Should be dislayed.


### 1.4 Launching the video server
This package does not directly stream or convert the rostopic stream. It first converts the rostopic to a video stream and sends it to Ia local IP and port.
This step converts the video stream to a web accessible stream.
This conversion is done via a ros package [ros_video_server](http://wiki.ros.org/web_video_server), but if you cloned and build this package it is included.
To launch this package:
```
roslaunch camera_image_exporter start_web_server.launch
```
To see if the stream converter has worked properly, the video stream is accessible via the browser.
Open a browser to "localhost:8080"

If you are running this via the Simcloud docker image, you the adress is  [docker container IP]:8080.
To find the docker container IP, run this command in a terminal outside of docker container
```
docker container list
```
Locate the container ID of the simcloud environment, where you are running the simulations. The insert this container ID into the following command.
```
docker inspect [container ID]
```
And find the IP adress. Then open a browser and direct it to [docker container IP]:8080 

### 1.5 Video Processing
This package van take the IP video stream and either stream the video or save the video as a recording, depending on which step you take, you may choose to go to **1.5.1** to stream to Youtube or **1.5.2** to save video.

### 1.5.1 Streaming video to youtube
To stream the video to youtube, you must first create a youtube streaming account. Navigate to the streaming page of youtube.
![Stream_key](https://user-images.githubusercontent.com/27964546/151963265-7eecb42e-5280-4ae2-b1a3-18fd949fe2b9.png)

After receiving your streaming key navigate to the streaming folder and open the example_key.conf
```
cd streaming
nano example_key
```
Your should see:
```
# Assign 
# Save this file as and change name from example_key.conf to key.conf
KEY="INSERT_KEY_HERE"
```
Replace INSERT_KEY_HERE with your streaming key.
Then save the file as "key.conf"

**PLEASE KEEP THIS KEY SECRET, INCLUDE IT key.conf IN YOUR GITIGNORE**

After creating your streaming key.
In this folder run the streaming script.

```
./youtube_stream.sh
```
### 1.5.2 Saving your videos
If you want to save your videos, repeat all the steps from Section **1.0 to 1.4**, and instead of the starting the stream. You will instead save the video.
The save video shell script allows you to choose the length of the video by using the flag -t followed by the amount of seconds you want to record.
**Example:**

```
./save_video.sh -t 100
```
Would record a video for 100 seconds. **If no time is given, the default is 10 seconds**

All the recorded videos are saved in the "camera_image_exporter/videos" directory.
