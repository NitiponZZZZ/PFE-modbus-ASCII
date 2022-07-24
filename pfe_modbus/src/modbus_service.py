#!/usr/bin/env python3
import rospy
from pfe_modbus.srv import fancontrol, chargecontrol, stopcontrol, fancontrolResponse, chargecontrolResponse, stopcontrolResponse
from modbus_driver import writeData


def callfan(request):
    writeData("fan", request.speedsent)
    return fancontrolResponse(request.speedsent)


def callstop(request):
    writeData("stop", request.stopsent)
    return stopcontrolResponse(request.stopsent)


def callcharge(request):
    writeData("charge", request.chargesent)
    return chargecontrolResponse(request.chargesent)


def speedcontrolService():
    rospy.init_node("control")
    servicefan = rospy.Service("fancontrol", fancontrol, callfan)
    servicestop = rospy.Service("stopcontrol", stopcontrol, callstop)
    servicecharge = rospy.Service("chargecontrol", chargecontrol, callcharge)
    rospy.spin()


if __name__ == '__main__':
    try:
        speedcontrolService()
    except rospy.ROSInterruptException:
        pass
