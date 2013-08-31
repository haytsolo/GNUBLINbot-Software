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
- Syntax überarbeiten (Gleiches Einrücken, ...) 
- Erzeugung der Steuersignale für den Servocontroller
- Erzeugung der Bewegungsabläufe (ohne optimierung - wie in der Skriptsteuerung)
- Ansteuerung mehrerer Servos gleichzeitig
- Senden der Signale an den Servocontroller


TODO:
- Test: Ob Software lauffähig auf GNUBLIN
- Test: Ob Kommandos korrekt übertragen und verarbeitet werden
- Erzeugung optimierter Bewegungsabläufe
- Fehlerbehandlung und Ausgabe in eine Error.txt
- Ausfürhliche Kommentare, Funktionskommentare

Hinweis:
Die Software auf dem Roboter muss als erstes ausgeführt werden!
