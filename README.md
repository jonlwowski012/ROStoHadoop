# ROS to Hadoop
## Overview

This package is used to read topics from ROS and store them as a CSV. The CSVs are then read into Hadoop.


## Important Files
- subscribe_to_keyword.py
   - This file will subscribe to a keyword and then write the information in associated topics into CSV files.
- hadoopPut.py
   - This file will read all of the CSV files in a directory and then store that information into Hadoop.
