#!/usr/bin/python
# -*- coding: utf-8 -*-

import gnublinbot_bot_init

def output(eingabe, sta_sto):
 if eingabe != 'Start/Stop' and sta_sto == True:

  if eingabe == 'Beenden':
   print 'Good Bye!'
   return 1
  #elif eingabe == '--help':
  # print 'Hilfetext TODO!'
  # return 0
  elif eingabe == 'Vorwärts':
   print 'Ich gehe gerade aus!'
   return 0
  elif eingabe == 'Rückwärts':
   print 'Ich gehe rückwärts!'
   return 0
  elif eingabe == 'Seitlich Links':
   print 'Ich gehe nach links!'
   return 0
  elif eingabe == 'Seitlich Rechts':
   print 'Ich gehe nach rechts!'
   return 0
  else:
   print 'Fehler: Falsche Eingabe!'
   return 0

 if eingabe == 'Beenden':
  print 'Good Bye!'
  return 1
 #elif eingabe == '--help':
 # print 'Hilfetext TODO!'
 # return 0
 elif eingabe == 'Start/Stop' and sta_sto == False:
  gnublinbot_bot_init.initialization()
  return 2
 elif eingabe == 'Start/Stop' and sta_sto == True:
  gnublinbot_bot_init.stop()
  return 2
 else:
  print "Bitte den Roboter erst mit Button 'Start/Stop' starten!"
