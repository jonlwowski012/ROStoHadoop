#!/usr/bin/env python
import os
import subprocess32 as subprocess

## Goal is to move a file from local storage to
#   HDFS for any file (argv1) to any HDFS directory (argv2)

# Currently has a file hardcoded in and a hdfs directory hardcoded
# Also is set up to continuously run until the file exceeds 1000 lines
#  before it sends the file to HDFS

# Making another that can be run once as well. Working on that this coming week

if __name__ == '__main__':
	count = 0
	num = 0
	while(True):
		#print os.path.exists("imu_data.csv")
		if(os.path.exists("imu_data.csv") == True):
			#print "File exisits counting lines"
			target = open("imu_data.csv", "r+")
			for line in target:
				count += 1
				print count
			if count >= 1000:
				print "Saving file to HDFS"
				target.close()
				subprocess.call(["hadoop", "fs", "-copyFromLocal", "imu_data.csv", "hdfs:///mikey/imu/imu_data"+str(num)])
				num+=1
				print "Deleting File"
				os.remove("imu_data.csv")
				count = 0
			else:
				target.close()
				
				