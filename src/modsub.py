#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import BatteryState
from pfe_modbus.msg import fanmsg, powersensormsg, statusmsg


def callback1(data):
    rospy.loginfo('Batt %s', data)


def callback2(data):
    rospy.loginfo('Status %s', data)


def callback3(data):
    rospy.loginfo('Fan %s', data)


def callback4(data):
    rospy.loginfo('Sensor %s', data)


def pfe_listener():
    rospy.init_node('modbusSup', anonymous=True)

    rospy.Subscriber('pfe_battery', BatteryState, callback1)
    #rospy.Subscriber('pfe_status', statusmsg, callback2)
    #rospy.Subscriber('pfe_fans', fanmsg, callback3)
   # rospy.Subscriber('pfe_power_sensors', powersensormsg, callback4)

    rospy.spin()


if __name__ == '__main__':
    pfe_listener()
