#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
#--
#-- File:                GNUBLINbot_bot.py
#--
#-- Description:
#-- Software for GnublinBot movement control.
#-- To be executed on the GNUBLINbot.
#--
#-- Change History:	Version: 24.04.2014
#--
#--
#-------------------------------------------------------------------------------
#-- Written by          Sebastian Sedlbauer
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

import socket   
import time
import logging

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

# Create TCP connection
s = socket.socket()         
port = 50000
s.bind(('', port))        
s.listen(5)     
log.info("Connection initialized and listening")           

    #def __init__(self, Port):
        #self.ser = serial.Serial(Port, baudrate=9600)

def moveServos(target0, target1, target2, target3, target4, target5, target6, target7, target8, target9, target10, target11):
    commandByte = chr(0x84) # Commando byte
    channelByte = chr(0x00) # First servonumber
    lowTargetByte0 = chr(target0 & 0x7F) # Target commando for the first servo (Upper Byte)
    highTargetByte0 = chr((target0 >> 7) & 0x7F) # (Lower Byte)
    lowTargetByte1 = chr(target1 & 0x7F) # Target commando for the second servo
    highTargetByte1 = chr((target1 >> 7) & 0x7F)
    lowTargetByte2 = chr(target2 & 0x7F)
    highTargetByte2 = chr((target2 >> 7) & 0x7F)
    lowTargetByte3 = chr(target3 & 0x7F)
    highTargetByte3 = chr((target3 >> 7) & 0x7F)
    lowTargetByte4 = chr(target4 & 0x7F)
    highTargetByte4 = chr((target4 >> 7) & 0x7F)
    lowTargetByte5 = chr(target5 & 0x7F)
    highTargetByte5 = chr((target5 >> 7) & 0x7F)
    lowTargetByte6 = chr(target6 & 0x7F)
    highTargetByte6 = chr((target6 >> 7) & 0x7F)
    lowTargetByte7 = chr(target7 & 0x7F)
    highTargetByte7 = chr((target7 >> 7) & 0x7F)
    lowTargetByte8 = chr(target8 & 0x7F)
    highTargetByte8 = chr((target8 >> 7) & 0x7F)
    lowTargetByte9 = chr(target9 & 0x7F)
    highTargetByte9 = chr((target9 >> 7) & 0x7F)
    lowTargetByte10 = chr(target10 & 0x7F)
    highTargetByte10 = chr((target10 >> 7) & 0x7F)
    lowTargetByte11 = chr(target11 & 0x7F)
    highTargetByte11 = chr((target11 >> 7) & 0x7F)
    
    # Commando to be sent to the servocontroller
    command = commandByte + channelByte + lowTargetByte0 + highTargetByte0 + lowTargetByte1 + highTargetByte1 + lowTargetByte2 + highTargetByte2 + lowTargetByte3 + highTargetByte3 + lowTargetByte4 + highTargetByte4 + lowTargetByte5 + highTargetByte5 + lowTargetByte6 + highTargetByte6 + lowTargetByte7 + highTargetByte7 + lowTargetByte8 + highTargetByte8 + lowTargetByte9 + highTargetByte9 + lowTargetByte10 + highTargetByte10 + lowTargetByte11 + highTargetByte11
    # self.ser.write(command)
    # self.ser.flush()
    log.info(command)
 
def movements_start():
    c.send('0')
    moveServos(6200, 7000, 7000, 5500, 5800, 0, 6300, 5000, 4300, 6500, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 7000, 6500, 5500, 5800, 0, 6300, 5000, 4800, 6500, 0, 6200)
    time.sleep(0.1)
    c.send('20')
    moveServos(6200, 7000, 6500, 6500, 5800, 0, 6300, 5000, 4800, 5700, 0, 6200)
    moveServos(6200, 6500, 6500, 6500, 5800, 0, 6300, 5500, 4800, 5700, 0, 6200)
    time.sleep(0.1)
    c.send('40')
    moveServos(6200, 6500, 5500, 6500, 5800, 0, 6300, 5500, 5800, 5700, 0, 6200)
    moveServos(6200, 6500, 5500, 6000, 5800, 0, 6300, 5500, 5800, 6300, 0, 6200)
    time.sleep(0.1)
    c.send('60')
    moveServos(6200, 6500, 5500, 6000, 5800, 0, 6300, 5500, 5800, 6300, 0, 6200)
    moveServos(6200, 6000, 5500, 6000, 5800, 0, 6300, 6000, 5800, 6300, 0, 6200)
    time.sleep(0.1)
    c.send('80')
    moveServos(6200, 6000, 4700, 6000, 5800, 0, 6300, 6000, 7000, 6300, 0, 6200)
    moveServos(6200, 6000, 4700, 5500, 5800, 0, 6300, 6000, 7000, 7200, 0, 6200)
    moveServos(6200, 6000, 4700, 5500, 5800, 0, 6300, 6000, 7000, 7200, 0, 6200)
    time.sleep(0.1)
    c.send('100')
    time.sleep(0.1)
    
def movements_stop():
    c.send('0')
    time.sleep(0.1)
    moveServos(6200, 6000, 4700, 5500, 5800, 0, 6300, 6000, 7000, 7200, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 6000, 4700, 6000, 5800, 0, 6300, 6000, 7000, 6300, 0, 6200)
    time.sleep(0.1)
    c.send('33')
    moveServos(6200, 6000, 5500, 6000, 5800, 0, 6300, 6000, 5800, 6300, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 6500, 5500, 6000, 5800, 0, 6300, 5500, 5800, 6300, 0, 6200)
    time.sleep(0.1)
    c.send('66')
    moveServos(6200, 6500, 5500, 5500, 5800, 0, 6300, 5500, 5800, 6500, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 6500, 7000, 5500, 5800, 0, 6300, 5500, 4300, 6500, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 6500, 7000, 5100, 5800, 0, 6300, 5500, 4300, 7200, 0, 6200)
    time.sleep(0.1)
    c.send('100')
    time.sleep(0.1)
        
def movements_forwards():
    c.send('0')
    moveServos(6200, 6000, 4700, 6100, 5800, 0, 6300, 6000, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 5200, 4700, 6100, 5800, 0, 6300, 6000, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 5200, 4700, 6100, 5800, 0, 6300, 5000, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 5200, 4700, 6100, 5800, 0, 6300, 5000, 7000, 7600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 6000, 4700, 6100, 5800, 0, 6300, 6000, 7000, 7600, 0, 6200)
    time.sleep(0.1)
    c.send('20')
    moveServos(6200, 6000, 4700, 6100, 5800, 0, 6300, 6000, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 6000, 4700, 6100, 5800, 0, 6300, 6800, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 7000, 4700, 6100, 5800, 0, 6300, 6800, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 7000, 4700, 5100, 5800, 0, 6300, 6800, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 6000, 4700, 5100, 5800, 0, 6300, 6000, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    c.send('40')
    moveServos(6200, 6000, 4700, 6100, 5800, 0, 6300, 6000, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 5200, 4700, 6100, 5800, 0, 6300, 6000, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 5200, 4700, 6100, 5800, 0, 6300, 5000, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 5200, 4700, 6100, 5800, 0, 6300, 5000, 7000, 7600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 6000, 4700, 6100, 5800, 0, 6300, 6000, 7000, 7600, 0, 6200)
    time.sleep(0.1)
    c.send('60')
    moveServos(6200, 6000, 4700, 6100, 5800, 0, 6300, 6000, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 6000, 4700, 6100, 5800, 0, 6300, 6800, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 7000, 4700, 6100, 5800, 0, 6300, 6800, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 7000, 4700, 5100, 5800, 0, 6300, 6800, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    c.send('80')
    moveServos(6200, 6000, 4700, 5100, 5800, 0, 6300, 6000, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 6000, 4700, 6100, 5800, 0, 6300, 6000, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 6000, 4700, 5500, 5800, 0, 6300, 6000, 7000, 7200, 0, 6200)
    time.sleep(0.1)
    c.send('100')
    time.sleep(0.1)

def movements_backwards():
    c.send('0')
    moveServos(6200, 6000, 4700, 6100, 5800, 0, 6300, 6000, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 6000, 4700, 5100, 5800, 0, 6300, 6000, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 7000, 4700, 5100, 5800, 0, 6300, 6000, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 7000, 4700, 5100, 5800, 0, 6300, 6800, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    c.send('20')
    moveServos(6200, 6000, 4700, 5100, 5800, 0, 6300, 6000, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 6000, 4700, 5100, 5800, 0, 6300, 6000, 7000, 7600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 6000, 4700, 5100, 5800, 0, 6300, 5000, 7000, 7600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 5200, 4700, 5100, 5800, 0, 6300, 5000, 7000, 7600, 0, 6200)
    time.sleep(0.1)
    c.send('40')
    moveServos(6200, 5200, 4700, 6100, 5800, 0, 6300, 5000, 7000, 7600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 6000, 4700, 6100, 5800, 0, 6300, 6000, 7000, 7600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 6000, 4700, 5100, 5800, 0, 6300, 6000, 7000, 7600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 7000, 4700, 5100, 5800, 0, 6300, 6000, 7000, 7600, 0, 6200)
    time.sleep(0.1)
    c.send('60')
    moveServos(6200, 7000, 4700, 5100, 5800, 0, 6300, 6800, 7000, 7600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 7000, 4700, 5100, 5800, 0, 6300, 6800, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 6000, 4700, 5100, 5800, 0, 6300, 6000, 7000, 6600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 6000, 4700, 5100, 5800, 0, 6300, 6000, 7000, 7600, 0, 6200)
    time.sleep(0.1)
    c.send('80')
    moveServos(6200, 6000, 4700, 5100, 5800, 0, 6300, 5000, 7000, 7600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 5200, 4700, 5100, 5800, 0, 6300, 5000, 7000, 7600, 0, 6200)
    time.sleep(0.1)
    moveServos(6200, 5200, 4700, 5500, 5800, 0, 6300, 5000, 7000, 7200, 0, 6200)
    time.sleep(0.1)
    c.send('100')
    time.sleep(0.1)

def movements_left():
    c.send('0')
    moveServos(6200, 6000, 4700, 5500, 5800, 0, 5300, 6000, 7000, 7200, 0, 6000)
    time.sleep(0.1)
    c.send('25')
    moveServos(6700, 6000, 4700, 5500, 7000, 0, 5300, 6000, 7000, 7200, 0, 6000)
    time.sleep(0.1)
    c.send('50')
    moveServos(6700, 6000, 4700, 5500, 7000, 0, 6300, 6000, 7000, 7200, 0, 6200)
    time.sleep(0.1)
    c.send('75')
    moveServos(6200, 6000, 4700, 5500, 5800, 0, 6300, 6000, 7000, 7200, 0, 6200)
    time.sleep(0.1)
    c.send('100')
    time.sleep(0.1)

def movements_right():
    c.send('0')
    moveServos(7200, 6000, 4700, 5500, 6000, 0, 6300, 6000, 7000, 7200, 0, 6200)
    time.sleep(0.1)
    c.send('25')
    moveServos(7200, 6000, 4700, 5500, 6000, 0, 5800, 6000, 7000, 7200, 0, 5000)
    time.sleep(0.1)
    c.send('50')
    moveServos(6200, 6000, 4700, 5500, 5800, 0, 5800, 6000, 7000, 7200, 0, 5000)
    time.sleep(0.1)
    c.send('75')
    moveServos(6200, 6000, 4700, 5500, 5800, 0, 6300, 6000, 7000, 7200, 0, 6200)
    time.sleep(0.1)
    c.send('100')
    time.sleep(0.1)


if __name__ == '__main__':
    first_start = 0
    # Starting position
    moveServos(6200, 7000, 7000, 5100, 5800, 0, 6300, 5000, 4300, 7200, 0, 6200)
    
    while True:    
        if first_start == 0:
            c, addr = s.accept()     
            c.send('connected')
            log.info("Connection established")
            first_start = 1
        else:
            log.info("Receiving commando")
            commando = c.recv(1024)
            if commando == 'start':
                log.info("Executing start commando ...")
                movements_start()
                c.send('executed')
                log.info("... executed!")
            if commando == 'stop':
                log.info("Executing stop commando ...")
                movements_stop()
                c.send('executed')
                log.info("... executed!")
            if commando == 'go_left':
                log.info("Executing go_left commando ...")
                movements_left()
                c.send('executed')
                log.info("... executed!")
            if commando == 'go_right':
                log.info("Executing go_right commando ...")
                movements_right()
                c.send('executed')
                log.info("... executed!")
            if commando == 'go_forwards':
                log.info("Executing go_forwards commando ...")
                movements_forwards()
                c.send('executed')
                log.info("... executed!")
            if commando == 'go_backwards':
                log.info("Executing go_backwards commando ...")
                movements_backwards()
                c.send('executed')
                log.info("... executed!")
            if commando == 'exit':
                log.info("Stopping ...")
                first_start = 0
                c.send('executed')
                log.info("... stopped!")
# Close the connection with the client
#c.close() 
