#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
#--
#-- File:                GNUBLINbot_pc.py
#--
#-- Description:
#-- Software for GnublinBot movement control.
#-- To be executed on a computer.
#--
#-- Change History:	Version: 24.04.2014
#--
#--
#-------------------------------------------------------------------------------
#-- Written by          Sebastian Sedlbauer
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

import os
import sys
from QtVariant import QtGui
from QtVariant import QtCore
from QtVariant import QtLoadUI
import logging
import time
import socket

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class BotError(Exception):
    pass


class MainWidget(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon(os.path.join('src', 'bot.ico')))

        self.start_stop_active = {"start_stop_active": 0}

        # Set window design created with designer-qt4
        ui_file = os.path.join("src", "GnublinBot.ui")
        QtLoadUI(ui_file, self)

        # Create TCP connection
        self.s = socket.socket()         
        port = 50000   
        ip = '127.0.0.1'
        self.s.connect((ip, port))
        if self.s.recv(1024) == 'connected':
            log.info("Connection to GNUBLINbot established")
        else:
            log.info("Connection to GNUBLINbot NOT established")

        # Configure window with button-functions, images and title
        self.setup_ui()
        self.setWindowTitle("Gnublinbot GUI")

    # DESIGN window and button actions
    def setup_ui(self):
        # select button images
        self.__on_img = QtGui.QIcon(os.path.join("src", "button_start.png"))
        self.__off_img = QtGui.QIcon(os.path.join("src", "button_stop.png"))

        # set start image to button
        self.button_start_stop.setIcon(self.__on_img)
        
        # set progressbar
        self.movement_bar.setValue(0)

        # execute function when button press is released
        self.button_left.released.connect(self.go_left)
        self.button_right.released.connect(self.go_right)
        self.button_forwards.released.connect(self.go_forwards)
        self.button_backwards.released.connect(self.go_backwards)

        # Start/Stop button
        self.button_start_stop.released.connect(self.start_stop)

    # Button, Statusbar and Images
    def lock_buttons(self):
        log.info("Lock buttons.")
        self.button_left.setEnabled(False)
        self.button_right.setEnabled(False)
        self.button_forwards.setEnabled(False)
        self.button_backwards.setEnabled(False)
        
    def unlock_buttons(self):
        log.info("Unlock buttons.")
        self.button_left.setEnabled(True)
        self.button_right.setEnabled(True)
        self.button_forwards.setEnabled(True)
        self.button_backwards.setEnabled(True)

    def lock_start_stop(self):
        log.info("Lock start stop")
        self.button_start_stop.setEnabled(False)
        
    def unlock_start_stop(self):
        log.info("Unlock start stop")
        self.button_start_stop.setEnabled(True)

    def send_command(self, command):
        self.s.send(command)
        while True:
            commando_executed = self.s.recv(1024)
            if commando_executed != 'executed':
                self.movement_bar.setValue(int(commando_executed))
            elif commando_executed == 'executed':
                break
            else:
                log.info("Problem with commando execution")

    def start_stop(self):
        if self.start_stop_active["start_stop_active"] == 0:
            self.lock_start_stop()
            self.send_command('start')
            self.button_start_stop.setIcon(self.__off_img)
            self.unlock_buttons()
            self.unlock_start_stop()
            self.start_stop_active["start_stop_active"] = 1
        elif self.start_stop_active["start_stop_active"] == 1:
            self.lock_start_stop()
            self.send_command('stop')
            self.button_start_stop.setIcon(self.__on_img)
            self.lock_buttons()
            self.unlock_start_stop()
            self.start_stop_active["start_stop_active"] = 0
            self.send_command('exit')

    def go_left(self):
        log.info("Go left")
        self.lock_buttons()
        self.lock_start_stop()
        self.send_command('go_left')
        self.unlock_buttons()
        self.unlock_start_stop()

    def go_right(self):
        log.info("Go right")
        self.lock_buttons()
        self.lock_start_stop()
        self.send_command('go_right')
        self.unlock_buttons()
        self.unlock_start_stop()

    def go_forwards(self):
        log.info("Go forwards")
        self.lock_buttons()
        self.lock_start_stop()
        self.send_command('go_forwards')
        self.unlock_buttons()
        self.unlock_start_stop()

    def go_backwards(self):
        log.info("Go backwards")
        self.lock_buttons()
        self.lock_start_stop()
        self.send_command('go_backwards')
        self.unlock_buttons()
        self.unlock_start_stop()
        

def show_window():

    app = QtGui.QApplication(sys.argv)
    widget = MainWidget()
    #widget.resize(400, 200)
    widget.show()

    sys.exit(app.exec_())

def sigint_handler():
    log.info("Stop")

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    show_window()
