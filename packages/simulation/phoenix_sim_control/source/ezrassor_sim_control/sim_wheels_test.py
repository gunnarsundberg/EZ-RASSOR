#!/usr/bin/env python

"""A ROS node that tests if steering system has received the proper data.

Written by Gunnar Sundberg.
"""
import rospy
from geometry_msgs.msg import Twist

NODE = "sim_wheels_test"
TOPIC = "diff_drive_controller/cmd_vel"


def wheels_test_callback(twist):
    wheel_test_pass = True
    
    # Test that all components have data
    if twist.linear.x is None:
        wheel_data_pass = False
    if twist.linear.y is None:
        wheel_data_pass = False
    if twist.linear.z is None:
        wheel_data_pass = False
    if twist.angular.x is None:
        wheel_data_pass = False
    if twist.angular.y is None:
        wheel_data_pass = False
    if twist.angular.z is None:
        wheel_data_pass = False
    
    if wheel_test_pass:
        print(twist)
        print("Wheel data tests passed")
    else:
        print(twist)
        print("Wheel data tests failed")
    

def start_node():
    try:
        rospy.init_node(NODE, anonymous=True)
        rospy.Subscriber(TOPIC, Twist, wheels_test_callback)
        rospy.loginfo("Wheel input test initialized.")
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
