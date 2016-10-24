#!/usr/bin/env python

# Quadrotor Simulator
# Jonathan Lwowski 
# Email: jonathan.lwowski@gmail.com
# Unmanned Systems Lab
# The University of Texas at San Antonio


#########          Libraries         ###################
import sys
from std_msgs.msg import String
from std_msgs.msg import Header
import rospy
import math
import numpy as np
import time
from sensor_msgs.msg import Imu
import csv
import os


def imuCallback(data, args):
	split_string = args.split('/')
	topic_name = split_string[len(split_string)-1]
	namespace = split_string[1]
	

	main = "data"
	main_exists = os.path.isdir(main)
	if not main_exists:
		os.makedirs(main)


	topic_name_exists = os.path.isdir(main+'/'+topic_name)
	if not topic_name_exists:
		os.makedirs(main+'/'+topic_name)

	

	filename = main+'/'+topic_name+'/'+namespace+'.csv'
	file_exists = os.path.isfile(filename)
	with open(filename, 'a') as csv_file:
		headers = ['Time Stamp', 'Seq', 'Frame Id', 'Orientation X', 'Orientation Y', 'Orientation Z', 'Orientation W', 'Orientation Covariance', 'Angular Velocity X', 'Angular Velocity Y', 'Angular Velocity Z', 'Angular Velocity Covariance', 'Linear Acceleration X', 'Linear Acceleration Y', 'Linear Acceleration Z', 'Linear Acceleration Covariance' ]
		writer = csv.DictWriter(csv_file, fieldnames=headers, lineterminator='\n')
		if not file_exists:
        		writer.writeheader()  # file doesn't exist yet, write a header
		writer.writerow({'Time Stamp': data.header.stamp, 'Seq': data.header.seq, 'Frame Id': data.header.frame_id, 'Orientation X': data.orientation.x, 'Orientation Y': data.orientation.y, 'Orientation Z': data.orientation.z, 'Orientation W': data.orientation.w, 'Orientation Covariance': data.orientation_covariance, 'Angular Velocity X': data.angular_velocity.x, 'Angular Velocity Y': data.angular_velocity.y, 'Angular Velocity Z': data.angular_velocity.z, 'Angular Velocity Covariance': data.angular_velocity_covariance, 'Linear Acceleration X': data.linear_acceleration.x, 'Linear Acceleration Y': data.linear_acceleration.y, 'Linear Acceleration Z': data.linear_acceleration.z, 'Linear Acceleration Covariance': data.linear_acceleration_covariance})
		

def people_location_sub_all():
	topics = rospy.get_published_topics()
        for i in range(len(topics)):
            if "raw_imu" in topics[i][0] and "raw_imu/" not in topics[i][0]:
                rospy.Subscriber(topics[i][0],Imu,imuCallback, (topics[i][0]))
 

if __name__ == '__main__':
	rospy.init_node('people_location_combiner', anonymous=True)
        people_location_sub_all()
        try:
		while(1):
			a=1

			
			
			
			
			
	except rospy.ROSInterruptException: pass

