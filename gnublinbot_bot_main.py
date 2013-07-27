#!/usr/bin/python

import gnublinbot_bot_out
import socket

# Aufbau einer TCP Verbindung
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(("", 50000)) 
s.listen(1)

sta_sto = False # Roboter Status

while True:
	komm, addr = s.accept() # Verbindung mit anfragender Adresse akzeptieren
	while True: 
		data = komm.recv(1024) # Nachrichten Empfang
		nachricht = 'recieved'# Antwort an PC das Daten erhalten
		komm.send(nachricht) # Senden der Antwort an GNUBLINbot Control Center (PC)
		output = gnublinbot_bot_out.output(data, sta_sto) # Verarbeitung der Eingabe
		if output == 1: # Abfangen ob Roboter schon gestartet oder nicht
			break
		elif output == 2:
			sta_sto = not sta_sto

