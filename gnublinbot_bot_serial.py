#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial

class ServoController:
	#def __init__(self, Port):
		#self.ser = serial.Serial(Port, baudrate=9600)

	def moveServos(self, target0, target1, target2, target3, target4, target5, target6, target7, target8, target9, target10, target11):

		commandByte = chr(0x84) # Komanndo Byte
		channelByte = chr(0x00) # Servonummer (bei Verwendung des Kommandos für mehrere Servos immer der erste)
		lowTargetByte0 = chr(target0 & 0x7F) # Target Kommando für ersten Servo (Upper Byte)
		highTargetByte0 = chr((target0 >> 7) & 0x7F) # (Lower Byte)
		lowTargetByte1 = chr(target1 & 0x7F) # Target Kommando für zweiten Servo
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

		command = commandByte + channelByte + lowTargetByte0 + highTargetByte0 + lowTargetByte1 + highTargetByte1 + lowTargetByte2 + highTargetByte2 + lowTargetByte3 + highTargetByte3 + lowTargetByte4 + highTargetByte4 + lowTargetByte5 + highTargetByte5 + lowTargetByte6 + highTargetByte6 + lowTargetByte7 + highTargetByte7 + lowTargetByte8 + highTargetByte8 + lowTargetByte9 + highTargetByte9 + lowTargetByte10 + highTargetByte10 + lowTargetByte11 + highTargetByte11 # Erzeugung des an den Servocontroller zu sendenden Komanndos
       
		# self.ser.write(command)
		# self.ser.flush()
		print command
		return 0

#test = ServoController()
#test.moveServos(500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500)
