#!/usr/bin/env python
import rospy

def auto_drive(world_state, ros_util):
    """ Travel forward in a straight line. Avoid obstacles while maintaining heading. """
    
    while ros_util.auto_function_command != 0:
        while(world_state.state_flags['warning_flag'] == 1):
            ros_util.command_pub.publish(ros_util.commands['right'])
            ros_util.rate.sleep()
        while(world_state.state_flags['warning_flag'] == 2):
            ros_util.command_pub.publish(ros_util.commands['left'])
            ros_util.rate.sleep()
        
        ros_util.command_pub.publish(ros_util.commands['forward'])
        ros_util.rate.sleep()

    ros_util.command_pub.publish(ros_util.commands['null'])

def auto_drive_location(world_state, ros_util, location):
    """ Navigate to location. Avoid obstacles while moving toward location. """

    
    while world_state.state_flags['positionX'] != location[0] and world_state.state_flags['positionY'] != location [1]:
        pass


    


def auto_dig(world_state, ros_util, duration):
    """ Rotate both drums inward and drive forward for duration time in seconds. """

    while ros_util.auto_function_command != 0:
        while(world_state.state_flags['warning_flag_front'] == 1):
            ros_util.command_pub.publish(ros_util.commands['right'])
            ros_util.rate.sleep()
        while(world_state.state_flags['warning_flag_front'] == 2):
            ros_util.command_pub.publish(ros_util.commands['left'])
            ros_util.rate.sleep()
        
        ros_util.command_pub.publish(ros_util.commands['forward'] | ros_util.commands['front_dig'] | ros_util.commands['back_dig'])
        ros_util.rate.sleep()

    ros_util.command_pub.publish(ros_util.commands['null'])

def auto_dock(world_state, ros_util):
    """ Dock with the hopper. """
    pass

def auto_self_right(world_state, ros_util):
    """  """
    pass