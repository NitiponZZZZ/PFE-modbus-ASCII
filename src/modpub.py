#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import BatteryState
from modbus_driver import readData, writeData, readBattery, readStatus, batt
from pfe_modbus.msg import fanmsg, powersensormsg, statusmsg

battery = BatteryState()
status = statusmsg()
fan = fanmsg()
power = powersensormsg()


def formatData():

    status.Supply_status1 = readStatus()[0]
    status.Power_supply_health1 = readStatus()[1]
    status.Supply_status2 = readStatus()[2]
    status.Power_supply_health2 = readStatus()[3]
    status.Emergency_Switch = readStatus()[4]
    status.Control_Switch = readStatus()[5]

    fan.fan1Speed = readData(0)[0]
    fan.fan1Temp = readData(0)[1]
    fan.fan2Speed = readData(0)[2]
    fan.fan2Temp = readData(0)[3]

    power.CTRLPowerSensorW = readData(2)[0]
    power.CTRLPowerSensorI = readData(2)[1]
    power.CTRLPowerSensorV = readData(2)[2]
    power.PowerSensorW = readData(1)[0]
    power.PowerSensorI = readData(1)[1]
    power.PowerSensorV = readData(1)[2]


def formatBatt(n):
    readBattery(n)
    battery.serial_number = str(n)
    battery.voltage = batt[0]
    battery.current = batt[1]
    battery.charge = batt[2]
    battery.capacity = batt[3]
    battery.percentage = batt[4]


def pfe_publiser():
    pub_battery = rospy.Publisher('pfe_battery', BatteryState, queue_size=1)
    pub_status = rospy.Publisher('pfe_status', statusmsg, queue_size=1)
    pub_fan = rospy.Publisher('pfe_fans', fanmsg, queue_size=1)
    pub_power_sensor = rospy.Publisher(
        'pfe_power_sensors', powersensormsg, queue_size=1)

    rospy.init_node('modbusPub', anonymous=True)
    rate = rospy.Rate(50)
    n = 0
    while not rospy.is_shutdown():
        writeData(1, 1)
        formatData()
        formatBatt(n)

        pub_battery.publish(battery)
        pub_fan.publish(fan)
        pub_power_sensor.publish(power)
        pub_status.publish(status)
        rate.sleep()
        if n < 4:
            n += 1
        else:
            n = 0


if __name__ == '__main__':
    try:
        pfe_publiser()
    except rospy.ROSInterruptException:
        pass
