#!/usr/bin/env python

from __future__ import print_function
from gazebo_msgs.srv import GetModelState
from gazebo_msgs.msg import ModelState 
from gazebo_msgs.srv import SetModelState
from math import sqrt
import roslib
import sys
import rospy
from std_msgs.msg import String
import socket


def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False


class Block:
	def __init__(self, name, relative_entity_name):
	    self._name = name
            self._relative_entity_name = relative_entity_name





class pos_find:
    def __init__(self, distance = None):
        rospy.init_node('update_gazebo_model', anonymous=True)
        self.pos_x = 0
        self.pos_y = 0
        self.pos_z = 0
        self.ori_x = 0
        self.ori_y = 0
        self.ori_z = 0
        if(distance == None):
            self.distance = 3 

    def get_pos(self):    
        model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
        resp_coordinates = model_coordinates(block,"")
        self.pos_x = resp_coordinates.pose.position.x
        self.pos_y = resp_coordinates.pose.position.y
        self.pos_z = resp_coordinates.pose.position.z
        self.ori_x = resp_coordinates.pose.orientation.x
        self.ori_y = resp_coordinates.pose.orientation.y
        self.ori_z = resp_coordinates.pose.orientation.z
        self.ori_w = resp_coordinates.pose.orientation.w
    
    def __str__(self):
       	self.get_pos()
       	print("x:\t", self.pos_x,
                    "\ny:\t", str(self.pos_y),
                    "\nz:\t", str(self.pos_z),
                    "\nx:\t", str(self.ori_z),
                    "\ny:\t", str(self.ori_y),
                    "\nz:\t", str(self.ori_z),
                    "\nw:\t", str(self.ori_w))
       	return (" ")
        
    def update_gazebo_models(self):
	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		self.get_pos()
		state_msg = ModelState()
		state_msg.model_name = 'camera'
		state_msg.pose.position.x = self.pos_x - (self.distance**2)/(1.73205)
		state_msg.pose.position.y = self.pos_y - (self.distance**2)/(1.73205)
		state_msg.pose.position.z = self.pos_z + (self.distance**2)/(1.73205)
		state_msg.pose.orientation.x = 0
		state_msg.pose.orientation.y = 0.194709171154
		state_msg.pose.orientation.z = 0.194709171154
		state_msg.pose.orientation.w = 1
		rospy.wait_for_service('/gazebo/set_model_state')
		try:
			set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
			resp = set_state( state_msg )
		except rospy.ServiceException, e:
			print ("Service call failed: ")
		if(!isOpen(127.0.0.1,8080))
        rate.sleep()
if __name__ == '__main__':
	if(len(sys.argv)>1):
		block = str(sys.argv[1])
		print(block)
	else:
		print("Please add object to follow")
		sys.exit(1)
	position = pos_find()
	print(position)
    
	position.update_gazebo_models()      
