#!/usr/bin/env python3
import rospy
from pfe_modbus.srv import fancontrol, chargecontrol, stopcontrol, fancontrolResponse, chargecontrolResponse, stopcontrolResponse


def control_client(mode, val):
    rospy.init_node("call")
    if mode == "fan":
        Fancontrol = rospy.ServiceProxy("fancontrol", fancontrol)
        response = Fancontrol(val)
    if mode == "charge":
        Chargecontrol = rospy.ServiceProxy("chargecontrol", chargecontrol)
        response = Chargecontrol(val)
    if mode == "stop":
        Stopcontrol = rospy.ServiceProxy("stopcontrol", stopcontrol)
        response = Stopcontrol(val)


if __name__ == "__main__":
    pass
