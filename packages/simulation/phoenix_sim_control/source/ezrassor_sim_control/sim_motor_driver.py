#!/usr/bin/env python

"""A ROS node that simulates motor control on Florida Poly's 3R Rover.

Written by Gunnar Sundberg and Jonathan Dixon.
"""
import rospy
from geometry_msgs.msg import Twist

NODE = "sim_motor_driver"
TOPIC = "wheel_instructions"

def motor_callback(twist):
    if (twist.angular.z > 0):
        print("RELEASE break")
        print("Rotating wheel 1 FORWARD\nRotating wheel 2 BACKWARD\nRotating wheel 3 FORWARD\nRotating wheel 4 BACKWARD\n")
        # Actual motor control code will go here
    elif (twist.angular.z < 0):
        print("RELEASE break")
        print("Rotating wheel 1 BACKWARD\nRotating wheel 2 FORWARD\nRotating wheel 3 BACKWARD\nRotating wheel 4 FORWARD\n")
        # Actual motor control code will go here
    elif (twist.linear.x > 0):
        print("RELEASE break")
        print("Rotating wheel 1 FORWARD\nRotating wheel 2 FORWARD\nRotating wheel 3 FORWARD\nRotating wheel 4 FORWARD\n")
        # Actual motor control code will go here
    elif (twist.linear.x < 0):
        print("RELEASE break")
        print("Rotating wheel 1 BACKWARD\nRotating wheel 2 BACKWARD\nRotating wheel 3 BACKWARD\nRotating wheel 4 BACKWARD\n")
        # Actual motor control code will go here
    elif (twist.linear.x == 0 or twist.angular.z == 0):
        print("RELEASE wheel 1\nRELEASE wheel 2\nRELEASE wheel 3\nRELEASE wheel 4\n")
        print("ENGAGE brake")
        # Engage brake
    


def start_node():
    try:
        rospy.init_node(NODE, anonymous=True)
        rospy.Subscriber(TOPIC, Twist, motor_callback)
        rospy.loginfo("Motors driver initialized.")
        rospy.spin()

    except rospy.ROSInterruptException:
        pass