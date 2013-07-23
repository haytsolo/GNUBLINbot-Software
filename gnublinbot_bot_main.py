#!/usr/bin/python

import gnublinbot_bot_connect # bei Netzwerk Empfang
# import gnublinbot_bot_in # bei Keyboard Eingabe
#import gnublinbot_bot_out

#sta_sto = False

while True:
 eingabe = gnublinbot_bot_connect.eingangssignal() # bei Netzwerk Empfang
 print eingabe
  #eingabe = gnublinbot_bot_in.getit() # bei Keyboard Eingabe
 #output = gnublinbot_bot_out.output(eingabe, sta_sto)
 #if output == 1:
 # break
 #elif output == 2:
 # sta_sto = not sta_sto

