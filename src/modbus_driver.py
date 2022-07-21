#!/usr/bin/env python3
import random
import minimalmodbus

master = minimalmodbus.Instrument('/dev/pts/4', 1, minimalmodbus.MODE_ASCII)
master.serial.baudrate = 115200
master.serial.bytesize = 8
master.serial.stopbits = 1
master.serial.timeout = 0.05
master.clear_buffers_before_each_transaction = True

batt = [0, 0, 0, 0, 0]


def readBattery(index: bytes):
    if index == 0:
        batt[0] = master.read_register(0, 0, 3)
        batt[1] = master.read_register(1, 0, 3)
        batt[2] = master.read_register(2, 0, 3)
        batt[3] = master.read_register(3, 0, 3)
        batt[4] = master.read_register(4, 0, 3)
        return batt
    if index == 1:
        batt[0] = master.read_register(5, 0, 3)
        batt[1] = master.read_register(6, 0, 3)
        batt[2] = master.read_register(7, 0, 3)
        batt[3] = master.read_register(8, 0, 3)
        batt[4] = master.read_register(9, 0, 3)
        return batt
    if index == 2:
        batt[0] = master.read_register(10, 0, 3)
        batt[1] = master.read_register(11, 0, 3)
        batt[2] = master.read_register(12, 0, 3)
        batt[3] = master.read_register(13, 0, 3)
        batt[4] = master.read_register(14, 0, 3)
        return batt
    if index == 3:
        batt[0] = master.read_register(15, 0, 3)
        batt[1] = master.read_register(16, 0, 3)
        batt[2] = master.read_register(17, 0, 3)
        batt[3] = master.read_register(18, 0, 3)
        batt[4] = master.read_register(19, 0, 3)
        return batt
    if index == 4:
        batt[0] = master.read_register(20, 0, 3)
        batt[1] = master.read_register(11, 0, 3)
        batt[2] = master.read_register(22, 0, 3)
        batt[3] = master.read_register(23, 0, 3)
        batt[4] = master.read_register(24, 0, 3)
        return batt


def readStatus():
    Read_all = master.read_bits(0, 6, 2)
    return Read_all


def readData(type):

    if type == 0:
        Read_Fan1S = master.read_register(25, 0, 3)
        Read_Fan1T = master.read_register(26, 0, 3)
        Read_Fan2S = master.read_register(27, 0, 3)
        Read_Fan2T = master.read_register(28, 0, 3)
        return Read_Fan1S, Read_Fan1T, Read_Fan2S, Read_Fan2T

    if type == 1:    # ctrl_sensor
        Read_ctrl_W = master.read_register(29, 0, 3)
        Read_ctrl_I = master.read_register(30, 0, 3)
        Read_ctrl_V = master.read_register(31, 0, 3)
        return Read_ctrl_W, Read_ctrl_I, Read_ctrl_V

    if type == 2:    # power_sensor
        Read_pow_W = master.read_register(32, 0, 3)
        Read_pow_I = master.read_register(33, 0, 3)
        Read_pow_V = master.read_register(34, 0, 3)
        return Read_pow_W, Read_pow_I, Read_pow_V


def writeData(hold: bool, coils: bool):
    if hold:
        Voltage = random.randint(24900, 25000)
        Current = random.randint(19900, 20000)
        Charge = random.randint(290, 300)
        Capacity = random.randint(29900, 30000)
        Percentage = random.randint(90, 100)
        Fan1S = random.randint(5990, 6000)
        Fan1T = random.randint(35, 40)
        Fan2S = random.randint(5990, 6000)
        Fan2T = random.randint(35, 40)
        watt = random.randint(240, 250)
        I = random.randint(9, 11)
        V = random.randint(23, 25)

        master.write_register(0, Voltage, 0)
        master.write_register(1, Current, 0)
        master.write_register(2, Charge, 0)
        master.write_register(3, Capacity, 0)
        master.write_register(4, Percentage, 0)

        master.write_register(5, Voltage, 0)
        master.write_register(6, Current, 0)
        master.write_register(7, Charge, 0)
        master.write_register(8, Capacity, 0)
        master.write_register(9, Percentage, 0)

        master.write_register(10, Voltage, 0)
        master.write_register(11, Current, 0)
        master.write_register(12, Charge, 0)
        master.write_register(13, Capacity, 0)
        master.write_register(14, Percentage, 0)

        master.write_register(15, Voltage, 0)
        master.write_register(16, Current, 0)
        master.write_register(17, Charge, 0)
        master.write_register(18, Capacity, 0)
        master.write_register(19, Percentage, 0)

        master.write_register(20, Voltage, 0)
        master.write_register(21, Current, 0)
        master.write_register(22, Charge, 0)
        master.write_register(23, Capacity, 0)
        master.write_register(24, Percentage, 0)

        master.write_register(25, Fan1S, 0)
        master.write_register(26, Fan1T, 0)
        master.write_register(27, Fan2S, 0)
        master.write_register(28, Fan2T, 0)

        master.write_register(29, watt, 0)
        master.write_register(30, I, 0)
        master.write_register(31, V, 0)
        master.write_register(32, watt, 0)
        master.write_register(33, I, 0)
        master.write_register(34, V, 0)
    if coils:
        Supply_status_1 = 1
        Power_supply_health_1 = 1
        Supply_status_2 = 1
        Power_supply_health_2 = 1
        Emergency_Switch = 0
        Control_Switch = 1

        master.write_bit(0, Supply_status_1, 15)
        master.write_bit(1, Power_supply_health_1, 15)
        master.write_bit(2, Supply_status_2, 15)
        master.write_bit(3, Power_supply_health_2, 15)
        master.write_bit(4, Emergency_Switch, 15)
        master.write_bit(5, Control_Switch, 15)
    print("Write Mode ON")

    def requestCharge(value):
        master.write_bit(6, value, 15)
        print("requestCharge")

    def requestStop(value):
        master.write_bit(7, value, 15)
        print("requestStop")

    def fan2speedcontrol(value):
        master.write_register(35, value, 0)
        print("set fan speed : "+str(value))
