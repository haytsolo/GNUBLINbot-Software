#!/usr/bin/python

# import gnublinbot_bot_in # bei Keyboard Eingabe zum Test
import gnublinbot_bot_out
import socket

# Aufbau einer TCP Verbindung
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(("", 50000)) 
s.listen(1)

sta_sto = False

while True:
# eingabe = gnublinbot_bot_in.getit() # bei Keyboard Eingabe
# bei Netzwerk Empfang 
 komm, addr = s.accept() # Verbindung mit anfragender Adresse akzeptieren
 while True: 
  data = komm.recv(1024)
  # print "[%s] %s" % (addr[0], data) # Testausgabe
  nachricht = 'recieved'# Antwort an PC das Daten erhalten
  komm.send(nachricht) 
  output = gnublinbot_bot_out.output(data, sta_sto)
  if output == 1:
   break
  elif output == 2:
   sta_sto = not sta_sto

