#!/usr/bin/python
# -*- coding: utf-8 -*-

import gnublinbot_bot_init

def output(eingabe, sta_sto):
 if eingabe != 'x' and sta_sto == True:

  if eingabe == 'exit':
   print 'Good Bye!'
   return 1
  elif eingabe == '--help':
   print 'Hilfetext TODO!'
   return 0
  elif eingabe == 'w':
   print 'Ich gehe gerade aus!'
   return 0
  elif eingabe == 's':
   print 'Ich gehe rückwärts!'
   return 0
  elif eingabe == 'a':
   print 'Ich gehe nach links!'
   return 0
  elif eingabe == 'd':
   print 'Ich gehe nach rechts!'
   return 0
  else:
   print 'Falsche Eingabe! Bitte wasd benutzen!'
   return 0

 if eingabe == 'exit':
  print 'Good Bye!'
  return 1
 elif eingabe == '--help':
  print 'Hilfetext TODO!'
  return 0
 elif eingabe == 'x' and sta_sto == False:
  gnublinbot_bot_init.initialization()
  return 2
 elif eingabe == 'x' and sta_sto == True:
  gnublinbot_bot_init.stop()
  return 2
 else:
  print 'Bitte den Roboter erst mit x starten!'
