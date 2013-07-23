#!/usr/bin/python

import socket

global eingangssignal

# Aufbau einer TCP Verbindung
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(("", 50000)) 
s.listen(1)

# Methode zum Empfang von Steuersignalen
def eingangssignal():
        komm, addr = s.accept() # Verbindung mit anfragender Adresse akzeptieren
        while True: 
            data = komm.recv(1024)

            print "[%s] %s" % (addr[0], data) 
            einganssignal = data
            nachricht = 'recieved'# Antwort an PC das Daten erhalten
            komm.send(nachricht) 
	return eingangssignal

try: 
    while True: 
       eingangssignal()
       print eingangssignal
finally: 
    s.close()
