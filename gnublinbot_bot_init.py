#!/usr/bin/python

import gnublinbot_bot_serial

def first_init():
	print 'Gehe in Ausgangsstellung ...'
	run = gnublinbot_bot_serial.ServoController()
	run.moveServos(6200, 7000, 7000, 5100, 5800, 0, 6300, 5000, 4300, 7200, 0, 6200)
	print '... fertig!'

def initialization():
	print 'Ich initialisiere ...'
	run = gnublinbot_bot_serial.ServoController()
	run.moveServos(6200, 7000, 7000, 5500, 5800, 0, 6300, 5000, 4300, 6500, 0, 6200)
	run.moveServos(6200, 7000, 6500, 5500, 5800, 0, 6300, 5000, 4800, 6500, 0, 6200)
	run.moveServos(6200, 7000, 6500, 6500, 5800, 0, 6300, 5000, 4800, 5700, 0, 6200)
	run.moveServos(6200, 6500, 6500, 6500, 5800, 0, 6300, 5500, 4800, 5700, 0, 6200)
	run.moveServos(6200, 6500, 5500, 6500, 5800, 0, 6300, 5500, 5800, 5700, 0, 6200)
	run.moveServos(6200, 6500, 5500, 6000, 5800, 0, 6300, 5500, 5800, 6300, 0, 6200)
	run.moveServos(6200, 6500, 5500, 6000, 5800, 0, 6300, 5500, 5800, 6300, 0, 6200)
	run.moveServos(6200, 6000, 5500, 6000, 5800, 0, 6300, 6000, 5800, 6300, 0, 6200)
	run.moveServos(6200, 6000, 4700, 6000, 5800, 0, 6300, 6000, 7000, 6300, 0, 6200)
	run.moveServos(6200, 6000, 4700, 5500, 5800, 0, 6300, 6000, 7000, 7200, 0, 6200)
	run.moveServos(6200, 6000, 4700, 5500, 5800, 0, 6300, 6000, 7000, 7200, 0, 6200)
	print '... fertig!'

def stop():
	print 'ich stoppe ...'
	run = gnublinbot_bot_serial.ServoController()
	run.moveServos(6200, 6000, 4700, 5500, 5800, 0, 6300, 6000, 7000, 7200, 0, 6200)
	run.moveServos(6200, 6000, 4700, 6000, 5800, 0, 6300, 6000, 7000, 6300, 0, 6200)
	run.moveServos(6200, 6000, 5500, 6000, 5800, 0, 6300, 6000, 5800, 6300, 0, 6200)
	run.moveServos(6200, 6500, 5500, 6000, 5800, 0, 6300, 5500, 5800, 6300, 0, 6200)
	run.moveServos(6200, 6500, 5500, 5500, 5800, 0, 6300, 5500, 5800, 6500, 0, 6200)
	run.moveServos(6200, 6500, 7000, 5500, 5800, 0, 6300, 5500, 4300, 6500, 0, 6200)
	run.moveServos(6200, 6500, 7000, 5100, 5800, 0, 6300, 5500, 4300, 7200, 0, 6200)
	print '... fertig!'
