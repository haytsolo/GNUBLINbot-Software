GNUBLINbot-Software
===================

Software mit grafischer Oberfläche zur Steuerung des GNUBLINbot.

Ziel ist die Bewegungen des Roboters über das Drücken von Buttons von einem PC aus zu steueren.
Die Steuerkommandos werden per WLAN auf den Roboter übertragen und dort verarbeitet.

Bereits integriert:
- Grafische Oberfläche zum Ausführen auf dem PC mit Steuerbuttons
- Senden der Steuerdaten über ein Netzwerk per TCP
- Empfangen der Steuerdaten und Bestätigung des Empfangs
- Verarbeitungsroutine für die empfangenen Daten
- Erzeugung der Steuersignale für den Servocontroller
- Erzeugung der Bewegungsabläufe (weitere Optimierung nötig!)
- Ansteuerung mehrerer/aller Servos gleichzeitig
- Senden der Signale an den Servocontroller

TODO:
- Test mit Gnublinbot
- Erzeugung optimierter Bewegungsabläufe
- Fehlerbehandlung und Logdatei

Hinweis:
Der Roboter muss als erstes gebootet werden (bis OK-Blinksignale), bevor die Steuersoftware gestartet werden kann.
