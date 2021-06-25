#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from time import sleep
import time
from std_msgs.msg import String, Duration
import message_filters
from message_filters import TimeSynchronizer, Subscriber, Cache

def part():
	pub = rospy.Publisher('/my_robot/Differential_left_controller/cmd_vel', Twist, queue_size=5)
	pub2 = rospy.Publisher('/my_robot/Differential_right_controller/cmd_vel', Twist, queue_size=5)

	for i in range(3000):
		msg = Twist()
		msg.linear.x = 0.1
		pub.publish(msg)
		pub2.publish(msg)
		rospy.loginfo('Stage 1')
	for i in range(190):
		msg.linear.x = -0.2
		pub.publish(msg)
		msg.linear.x = 0.2
		pub2.publish(msg)
		rospy.loginfo('Turning')
	for i in range(4000):
		msg = Twist()
		msg.linear.x = 0.2
		pub.publish(msg)
		pub2.publish(msg)
		rospy.loginfo('Stage 2')
	for i in range(195):
		msg.linear.x = 0.2
		pub.publish(msg)
		msg.linear.x = -0.2
		pub2.publish(msg)
		rospy.loginfo('Turning')
	for i in range(1000):
		msg = Twist()
		msg.linear.x = 0.2
		pub.publish(msg)
		pub2.publish(msg)
		rospy.loginfo('Stage 3')
	for i in range(195):
		msg.linear.x = 0.2
		pub.publish(msg)
		msg.linear.x = -0.2
		pub2.publish(msg)
		rospy.loginfo('Turning')
	for i in range(500):
		msg = Twist()
		msg.linear.x = 0.2
		pub.publish(msg)
		pub2.publish(msg)
		rospy.loginfo('Stage 4')
	for i in range(195):
		msg.linear.x = -0.2
		pub.publish(msg)
		msg.linear.x = 0.2
		pub2.publish(msg)
		rospy.loginfo('Turning')
	for i in range(1500):
		msg = Twist()
		msg.linear.x = 0.2
		pub.publish(msg)
		pub2.publish(msg)
		rospy.loginfo('Stage 5')
	for i in range(195):
		msg.linear.x = 0.2
		pub.publish(msg)
		msg.linear.x = -0.2
		pub2.publish(msg)
		rospy.loginfo('Turning')
	for i in range(500):
		msg = Twist()
		msg.linear.x = 0.2
		pub.publish(msg)
		pub2.publish(msg)
		rospy.loginfo('Stage 5')
	for i in range(1000000):
		msg = Twist()
		msg.linear.x = 0
		pub.publish(msg)
		pub2.publish(msg)
		rospy.loginfo('Finish !')

if __name__ == '__main__':

		rospy.init_node('node', anonymous=True)
		part()
		rospy.spin()
