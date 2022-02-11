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
You may test this by manually moving the object in Gazebo:


### 1.2 Viewing the video stream
If launched succesffuly the video stream topic can be viewed via:
```
rostopic list
```

The topic "/camera/image_raw" should be dislayed.


### 1.4 Launching the video server
This step converts the video stream to a web accessible stream.
```
roslaunch camera_image_exporter start_web_server.launch
```
This stream can be view by openign a browser to "localhost:8080"

### 1.5 Streaming video to youtube
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
### 1.6 Saving your videos
If you want to save your videos, repeat all the steps from Section **1.0 to 1.4**, and instead of the starting the stream. You will instead save the video.
The save video shell script allows you to choose the length of the video by using the flag -t followed by the amount of seconds you want to record.
**Example:**

```
./save_video.sh -t 100
```
Would record a video for 100 seconds. **If no time is given, the default is 10 seconds**

All the recorded videos are saved in the "camera_image_exporter/videos" directory.
