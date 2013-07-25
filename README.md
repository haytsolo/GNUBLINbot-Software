GNUBLINbot-Software
===================

Software zur Steuerung des GNUBLINbot.

Ziel ist die Bewegungen des Roboters über eine grafische Oberfläche (GNUBLINbot Control Center) auf einem PC zu steueren.
Die Steuersignale werden per WLAN auf den Roboter übertragen und dort verarbeitet.

Bereits integriert:
- Grafische Oberfläche zum ausführen auf dem PC mit Steuerbuttons
- Senden der Steuerdaten über ein Netzwerk per TCP
- Empfangen der Steuerdaten und Bestätigung des Empfangs
- Verarbeitungsroutine für die empfangenen Daten

TODO:
- Test: Senden der Signale an den Servocontroller
- Test: Erzeugung der Steuersignale für den Servocontroller
- Erzeugung der Bewegungsabläufe
- Fehlerbehandlung und Ausgabe in eine Error.txt
- Verbesserung der Bewegungsabläufe und Ansteuerung vom mehreren Servos gleichzeitig
- Syntax überarbeiten (Gleiches Einrücken, ...) 
