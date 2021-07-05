# Gazebo-ROS-SLAM-customize-robot
### This repositories is further developed from https://github.com/laitathei/Gazebo-customize-robot
### This guideline followed https://blog.csdn.net/zxl970921/article/details/114982558 work
### Installation for rtabmap_ros packages in ROS
```XML
git clone https://github.com/introlab/rtabmap.git rtabmap
mkdir -p ~/rtabmap_ws/src 
cd ..           
cd ~/rtabmap_ws                                         
catkin_make
sudo gedit ~/.bashrc
```
### Add `source ~/rtabmap_ws/devel/setup.bashrc` at the end of the file
### Open another terminal and type following command
```XML
sudo apt-get install ros-melodic-rtabmap ros-melodic-rtabmap-ros
sudo apt-get remove ros-melodic-rtabmap ros-melodic-rtabmap-ros
cd rtabmap/build
cmake -DCMAKE_INSTALL_PREFIX=~/rtabmap_ws/devel ..
make -j4
make install
cd ~/rtabmap_ws
git clone https://github.com/introlab/rtabmap_ros.git src/rtabmap_ros
catkin_make
```
### If you are successed to install rtabmap_ros packages, you should saw the following photo
![image](https://github.com/laitathei/Gazebo-ROS-SLAM-customize-robot/blob/main/demo.jpeg)
### Correct the rtabmap.launch file line 57 to line 61 to following
```XML
  <!-- RGB-D related topics -->
  <arg name="rgb_topic"               default="/camera/color/image_raw" />
  <arg name="depth_topic"             default="/camera/aligned_depth_to_color/image_raw" />
  <arg name="camera_info_topic"       default="/camera/color/camera_info" />
  <arg name="depth_camera_info_topic" default="$(arg camera_info_topic)" />
```
### Test the performance
```XML
roslaunch realsense2_camera rs_rgbd.launch 
roslaunch rtabmap_ros rtabmap.launch rtabmap_args:="--delete_db_on_start"
```
### Installation for gmapping package of melodic version
```XML
sudo apt-get install ros-melodic-gmapping
```
### Please ensure the laser scan topic is published before to record the map
### Choose map as the fix frame in rviz and add the robotmodel and laser scan topic to rviz
### Once you start the process, you should scan all obstacle and save the map via following command
```XML
rosrun map_server map_saver -f map
```
### Two way to record the map
1. gmapping and AMCL package
2. Rtabmap
Remark: this repositories used the method one

