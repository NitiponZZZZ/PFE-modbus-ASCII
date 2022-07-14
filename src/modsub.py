#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def callback1(data):
    rospy.loginfo('Batt %s', data.data)


def callback2(data):
    rospy.loginfo('fan %s', data.data)


def callback3(data):
    rospy.loginfo('ctrl %s', data.data)


def callback4(data):
    rospy.loginfo('power %s', data.data)


def callback5(data):
    rospy.loginfo('status %s', data.data)


def pfe_listener():
    rospy.init_node('modbusSup', anonymous=True)

    rospy.Subscriber('pfe_battery', String, callback1)
    rospy.Subscriber('pfe_fans', String, callback2)
    rospy.Subscriber('pfe_sensors_ctrl', String, callback3)
    rospy.Subscriber('pfe_sensors_power', String, callback4)
    rospy.Subscriber('pfe_status', String, callback5)

    rospy.spin()


if __name__ == '__main__':
    pfe_listener()
