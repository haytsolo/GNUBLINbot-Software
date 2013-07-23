#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import der PyGTK2 Module und Initialisierung der GTK+ Environment
import pygtk
pygtk.require('2.0') # Test auf Version ab 2.0
import gtk
# Modul für eine TCP Verbindung über das Netzwerk
import socket
# Modul für zeitlich gesteuerte Abläufe
import time

# Verbindunsdaten und Aufbau einer TCP Verbindung
ip = '127.0.0.1' # IP des Roboters (Bei lokalem Test am PC 127.0.0.1)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((ip, 50000))

class gui:

# Callback Funktionen
# Verarbeitung der Click-Events
 def senddata(self, widget, data):
  if data == 'button1':
   while True: 
    nachricht = 'Vorwärts' 
    s.send(nachricht) # Senden der Nachricht zum Roboter
    time.sleep(1) # Wartezeit bis Antwort erwartet wird
    antwort = s.recv(1024) # Antwort vom Roboter
    if antwort == 'recieved': # Abbruch des Sendens
     break
  elif data == 'button2':
   while True: 
    nachricht = 'Seitlich Links' 
    s.send(nachricht) 
    time.sleep(1)
    antwort = s.recv(1024) 
    if antwort == 'recieved':
     break
  elif data == 'button3':
   while True: 
    nachricht = 'Start/Stop' 
    s.send(nachricht) 
    time.sleep(1)
    antwort = s.recv(1024) 
    if antwort == 'recieved':
     break
  elif data == 'button4':
   while True: 
    nachricht = 'Seitlich Rechts' 
    s.send(nachricht) 
    time.sleep(1)
    antwort = s.recv(1024) 
    if antwort == 'recieved':
     break
  elif data == 'button5':
   while True: 
    nachricht = 'Rückwärts' 
    s.send(nachricht) 
    time.sleep(1)
    antwort = s.recv(1024) 
    if antwort == 'recieved':
     break
  elif data == 'button6':
   while True: 
    nachricht = 'Beenden' 
    s.send(nachricht) 
    time.sleep(1)
    antwort = s.recv(1024) 
    if antwort == 'recieved':
     break

# Verarbeitung eine Button-Press_events auf den Exit Button
 def destroy(self, widget, data=None):
  gtk.main_quit()

# Verarbeitung der Signale vom Window Manager ("close")
 def delete_event(self, widget, event, data=None): # data wird ignoriert
  return False # Bei Fals als Rückgabewert Aufruf von "destroy"

# Methode zur Initialisierung des Toplevel Windows und der Buttons
 def __init__(self):
  self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
  self.window.set_title("GNUBLINbot Control Center")
  self.window.connect("delete_event", self.delete_event) # Aufruf der Methode für "close"
  self.window.connect("destroy", self.destroy) # Aufruf der Methode für "exit"-Button
  self.window.set_border_width(10) # "Rahmen"-Breite
#Boxen erstellen
  self.box1 = gtk.VBox(False, 0) # Erstellen der horizontalen Box zum Einfügen der Widgets (z.B. Buttons)
  self.box2 = gtk.HBox(False, 0) # Erstellen der vertikalen Box zum Einfügen der Widgets
  self.box3 = gtk.HBox(False, 0) # Erstellen der vertikalen Box zum Einfügen der Widgets
  self.box4 = gtk.HBox(False, 0) # Erstellen der vertikalen Box zum Einfügen der Widgets
  self.window.add(self.box1) # Box in Fenster einfügen
  self.box1.pack_start(self.box2, False, False, 0)
  self.box1.pack_start(self.box3, False, False, 0)
  self.box1.pack_start(self.box4, False, False, 0)

# Button 1
  self.button1 = gtk.Button("Vorwärts") # Button-Label
  self.button1.connect("clicked", self.senddata, "button1") # Button-"clicked"-Event mit Methode zur Verarbeitung verbinden
  self.box2.pack_start(child=self.button1, expand=True, fill=False, padding=0) # Button in das Fenster (bzw. Container) integrieren
  self.button1.show() # Button anzeigen

# Button 2
  self.button2 = gtk.Button("Seitlich Links")
  self.button2.connect("clicked", self.senddata, "button2")
  self.box3.pack_start(self.button2, True, False, 0)
  self.button2.show()

# Button 3
  self.button3 = gtk.Button(" Start & Stop ")
  self.button3.connect("clicked", self.senddata, "button3")
  self.box3.pack_start(self.button3, True, True, 0)
  self.button3.show()

# Button 4
  self.button4 = gtk.Button("Seitlich Rechts")
  self.button4.connect("clicked", self.senddata, "button4")
  self.box3.pack_start(self.button4, True, False, 0)
  self.button4.show()

# Button 5
  self.button5 = gtk.Button("Rückwärts")
  self.button5.connect("clicked", self.senddata, "button5")
  self.box4.pack_start(self.button5, True, False, 0)
  self.button5.show()
 
# Seperator horizontal
  separator = gtk.HSeparator()
  self.box1.pack_start(separator, False, True, 20)
  separator.show()

# Button 6
  self.button6 = gtk.Button("Beenden")
  self.button6.connect_object("clicked", gtk.Widget.destroy, self.window)
  self.box1.pack_start(self.button6, True, True, 0)
  self.button6.show()

  self.box1.show() # Box 1 anzeigen
  self.box2.show() # Box 2 anzeigen
  self.box3.show() # Box 3 anzeigen
  self.box4.show() # Box 4 anzeigen
  self.window.show() # Fenster anzeigen

# Methode zum Aufruf des GTK+ Event Processing (Maus-, Tastatur-, Window-Events)
def gnublinbot_main():
 gtk.main()

# Prüfung ob Programm direkt in Python ausgeführt wird und Instanziierung
if __name__ == "__main__":
     gnublinbot = gui()
     gnublinbot_main() # Start der Oberfläche und Warten auf Events

