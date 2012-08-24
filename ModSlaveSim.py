#-------------------------------------------------------------------------------
# Name:        ModSlaveSim
# Purpose:
#
# Author:      elbar
#
# Created:     26/03/2012
# Copyright:   (c) elbar 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#add logging capability
import logging
#repeated timer
import RepeatTimer as rt
import random
#modbus toolkit
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus as modbus
import modbus_tk.modbus_tcp as modbus_tcp
import modbus_tk.modbus_rtu as modbus_rtu
#serial communication
import serial
#logger
logger = modbus_tk.utils.create_logger("console")

#-------------------------------------------------------------------------------
def ModServerFactory(args):

    __modServer = None

    if args[0]=='-tcp':
        logger.info("Build TCP Server - Port: {0}".format(args[1]))
        try :
            __modServer = modbus_tcp.TcpServer(int(args[1]))
        except Exception,msg:
            logger.error("Error while building TCP Server : {0}".format(msg))
    elif args[0]=='-rtu':
        logger.info("Build RTU Server - Port: {0}, Baudrate: {1}, Bytesize: {2}, Parity: {3}, Stopbits : {4}"
                    .format(args[1],args[2],args[3],args[4],args[5]))
        try:
            __modServer = modbus_rtu.RtuServer(serial.Serial(port=int(args[1]),
                                                        baudrate=int(args[2]),
                                                        bytesize=int(args[3]),
                                                        parity=args[4],
                                                        stopbits=float(args[5]),
                                                        xonxoff=0))
        except Exception,msg:
            logger.error("Error while building RTU Server : {0}".format(msg))
    else:
        logger.error("Wrong arguments")

    return __modServer
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
class ModSlaveSim(object):

    def __init__(self,modServer,slaveAddress,timeIntervalSim,
                    no_coils = 50, no_dig_inputs = 50,
                    no_input_regs = 50, no_hold_regs = 50):
        self.__modServer = modServer
        self._no_coils = no_coils
        self._no_dig_inputs = no_dig_inputs
        self._no_input_regs = no_input_regs
        self._no_hold_regs = no_hold_regs
        try:
            #add slave
            self.slave= modServer.add_slave(slaveAddress)
            #add blocks
            self.slave.add_block('0', cst.COILS , 0, self._no_coils)
            self.slave.add_block('1', cst.DISCRETE_INPUTS, 0, self._no_dig_inputs)
            self.slave.add_block('3', cst.ANALOG_INPUTS , 0, self._no_input_regs)
            self.slave.add_block('4', cst.HOLDING_REGISTERS, 0, self._no_hold_regs)
            #create timer
            self.__timer=rt.RepeatTimer(timeIntervalSim,self.__simBlockValues,0)
        except Exception,msg:
    		logger.error("Slave Init Error : {0}".format(msg))

    def start(self):
        logger.info("Slave sim started")
        self.__timer.start()

    def stop(self):
        logger.info("Slave sim stopped")
        self.__timer.cancel()

    def __simBlockValues(self):
        #init block values
        block0=[]#coils
        block1=[]#discrete inputs
        block3=[]#analog inputs
        block4=[]#holding registers
        #coils
        for i in range(0,self._no_coils):
            block0.append(random.randrange(0,2,1))
        self.slave.set_values('0',0,block0)
        #discrete inputs
        for i in range(0,self._no_dig_inputs):
            block1.append(random.randrange(0,2,1))
        self.slave.set_values('1',0,block1)
        #analog inputs
        for i in range(0,self._no_input_regs):
            block3.append(random.randrange(0,100,1))
        self.slave.set_values('3',0,block3)
        #holding registers
        for i in range(0,self._no_hold_regs):
            block4.append(random.randrange(0,100,1))
        self.slave.set_values('4',0,block4)
#-------------------------------------------------------------------------------
