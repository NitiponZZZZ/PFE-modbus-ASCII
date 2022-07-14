#!/usr/bin/env python3
from socket import MsgFlag
import rospy
from std_msgs.msg import Int8MultiArray, Int16MultiArray
from sensor_msgs.msg import BatteryState
from modbus_driver import readData, writeData, readBattery, readStatus, batt0, batt1, batt2, batt3, batt4
from pfe_modbus.msg import fanmsg

battery = BatteryState()

status = Int8MultiArray()
fan = fanmsg()
ctrl = Int16MultiArray()
power = Int16MultiArray()


def formatData():
    readBattery(0)
    battery.serial_number = '0'
    battery.voltage = batt0[0]
    battery.current = batt0[1]
    battery.charge = batt0[2]
    battery.capacity = batt0[3]
    battery.percentage = batt0[4]

    readBattery(1)
    battery.serial_number = '1'
    battery.voltage = batt1[0]
    battery.current = batt1[1]
    battery.charge = batt1[2]
    battery.capacity = batt1[3]
    battery.percentage = batt1[4]

    readBattery(2)
    battery.serial_number = '2'
    battery.voltage = batt2[0]
    battery.current = batt2[1]
    battery.charge = batt2[2]
    battery.capacity = batt2[3]
    battery.percentage = batt2[4]

    readBattery(3)
    battery.serial_number = '3'
    battery.voltage = batt3[0]
    battery.current = batt3[1]
    battery.charge = batt3[2]
    battery.capacity = batt3[3]
    battery.percentage = batt3[4]

    readBattery(4)
    # battery.header.stamp += 1
    battery.serial_number = '4'
    battery.voltage = batt4[0]
    battery.current = batt4[1]
    battery.charge = batt4[2]
    battery.capacity = batt4[3]
    battery.percentage = batt4[4]

    status.data = readStatus()

    fan.fan1Speed = readData(0)[0]
    fan.fan1Temp = readData(0)[1]
    fan.fan2Speed = readData(0)[2]
    fan.fan2Temp = readData(0)[3]

    ctrl.data = readData(1)
    power.data = readData(2)


def pfe_publiser():
    pub_battery = rospy.Publisher('pfe_battery', BatteryState, queue_size=10)
    pub_status = rospy.Publisher('pfe_status', Int8MultiArray, queue_size=10)
    pub_fan = rospy.Publisher('pfe_fans', fanmsg, queue_size=10)
    pub_ctrl = rospy.Publisher(
        'pfe_sensors_ctrl', Int16MultiArray, queue_size=10)
    pub_power = rospy.Publisher(
        'pfe_sensors_power', Int16MultiArray, queue_size=10)
    rospy.init_node('modbusPub', anonymous=True)
    rate = rospy.Rate(50)

    while not rospy.is_shutdown():
        # writeData(1, 1)
        formatData()

        pub_battery.publish(battery)
        pub_fan.publish(fan)
        pub_ctrl.publish(ctrl)
        pub_power.publish(power)
        pub_status.publish(status)
        rate.sleep()


if __name__ == '__main__':
    try:
        pfe_publiser()
    except rospy.ROSInterruptException:
        pass
