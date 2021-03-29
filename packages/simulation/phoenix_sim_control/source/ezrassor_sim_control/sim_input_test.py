#!/usr/bin/env python

"""A ROS node that tests if user input has been received by the sysem.

Written by Gunnar Sundberg.
"""
import rospy
from geometry_msgs.msg import Twist

NODE = "sim_input_test"
TOPIC = "wheel_instructions"
MAX_VELOCITY = 5


def input_test_callback(input):
    if input:
        print("Input received")
    else:
        print("Input not received")
    

def start_node():
    try:
        rospy.init_node(NODE, anonymous=True)
        rospy.Subscriber(TOPIC, Twist, input_test_callback)
        rospy.loginfo("Simulation input test initialized.")
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
