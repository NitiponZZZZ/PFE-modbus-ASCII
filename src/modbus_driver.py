#!/usr/bin/env python3
import random
import minimalmodbus

master = minimalmodbus.Instrument('/dev/pts/4', 1, minimalmodbus.MODE_ASCII)
master.serial.baudrate = 115200         # Baud
master.serial.bytesize = 8
master.serial.stopbits = 1
master.serial.timeout = 0.1          # seconds
master.clear_buffers_before_each_transaction = True

batt0 = [0, 0, 0, 0, 0]
batt1 = [0, 0, 0, 0, 0]
batt2 = [0, 0, 0, 0, 0]
batt3 = [0, 0, 0, 0, 0]
batt4 = [0, 0, 0, 0, 0]


def readBattery(index: bytes):
    if index == 0:
        batt0[0] = master.read_register(0, 0, 3)
        batt0[1] = master.read_register(1, 0, 3)
        batt0[2] = master.read_register(2, 0, 3)
        batt0[3] = master.read_register(3, 0, 3)
        batt0[4] = master.read_register(4, 0, 3)
        return batt0
    if index == 1:
        batt1[0] = master.read_register(5, 0, 3)
        batt1[1] = master.read_register(6, 0, 3)
        batt1[2] = master.read_register(7, 0, 3)
        batt1[3] = master.read_register(8, 0, 3)
        batt1[4] = master.read_register(9, 0, 3)
        return batt1
    if index == 2:
        batt2[0] = master.read_register(10, 0, 3)
        batt2[1] = master.read_register(11, 0, 3)
        batt2[2] = master.read_register(12, 0, 3)
        batt2[3] = master.read_register(13, 0, 3)
        batt2[4] = master.read_register(14, 0, 3)
        return batt2
    if index == 3:
        batt3[0] = master.read_register(15, 0, 3)
        batt3[1] = master.read_register(16, 0, 3)
        batt3[2] = master.read_register(17, 0, 3)
        batt3[3] = master.read_register(18, 0, 3)
        batt3[4] = master.read_register(19, 0, 3)
        return batt3
    if index == 4:
        batt4[0] = master.read_register(20, 0, 3)
        batt4[1] = master.read_register(11, 0, 3)
        batt4[2] = master.read_register(22, 0, 3)
        batt4[3] = master.read_register(23, 0, 3)
        batt4[4] = master.read_register(24, 0, 3)
        return batt4


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

        master.write_register(29, Fan1S, 0)
        master.write_register(30, Fan1T, 0)
        master.write_register(31, Fan2S, 0)
        master.write_register(32, Fan2T, 0)
    if coils:
        Supply_status = random.randint(0, 1)
        Power_supply_health = random.randint(0, 1)
        Emergency_Switch = random.randint(0, 1)
        Control_Switch = random.randint(0, 1)
        Need_Charge = random.randint(0, 1)
        Need_Stop = random.randint(0, 1)

        master.write_bit(0, Supply_status, 15)
        master.write_bit(1, Power_supply_health, 15)
        master.write_bit(2, Emergency_Switch, 15)
        master.write_bit(3, Control_Switch, 15)
        master.write_bit(4, Need_Charge, 15)
        master.write_bit(5, Need_Stop, 15)
    print("Write Mode ON")
