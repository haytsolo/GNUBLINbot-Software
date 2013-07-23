#!/usr/bin/python

import gnublinbot_bot_in
import gnublinbot_bot_out

sta_sto = False

while True:
 eingabe = gnublinbot_bot_in.getit()
 output = gnublinbot_bot_out.output(eingabe, sta_sto)
 if output == 1:
  break
 elif output == 2:
  sta_sto = not sta_sto

