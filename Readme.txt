Dieser Taschenrechner ist eine einfache Desktop-Anwendung, die mit PyQt5 erstellt wurde. Sie ermöglicht grundlegende mathematische Berechnungen sowie die Anzeige des Berechnungsverlaufs.

Funktionen
- Mathematische Berechnungen: Unterstützt grundlegende Operationen wie Addition, Subtraktion, Multiplikation und Division.
- Berechnungsverlauf: Zeigt die letzten 7 Berechnungen an.
- Tasten für Clear und DEL: Ermöglicht das Löschen der gesamten Eingabe oder des letzten Zeichens.
- Eingabebeschränkung: Der Taschenrechner erlaubt nur die Eingabe von Zahlen und mathematischen Operatoren.
- Direkte Berechnung durch Drücken der Enter-Taste.

Voraussetzungen:
- Python 3.x
- PyQt5 muss installiert sein

Dateien:
- Taschenrechner_ui.py: Die generierte UI-Datei des Taschenrechners.
- taschenrechner.py: Die Hauptlogik des Taschenrechners (dieses Skript).

Verwendung
- Führe die Datei taschenrechner.py aus, um das Taschenrechner-Programm zu starten.
- Gib eine mathematische Berechnung in das Textfeld ein und drücke entweder Enter oder den Button Berechnen, um das Ergebnis anzuzeigen.
- Der LCD-Bildschirm zeigt das Ergebnis der Berechnung an. Der Verlauf speichert die letzten 7 Berechnungen.
- Mit dem Clear-Button kannst du das Eingabefeld und den Verlauf zurücksetzen. Der DEL-Button entfernt das letzte Zeichen in der aktuellen Eingabe.

Benutzeroberfläche
- Eingabefeld: Textfeld zur Eingabe des mathematischen Ausdrucks.
- Berechnen-Button: Klick darauf, um die Berechnung durchzuführen.
- LCD-Anzeige: Zeigt das Ergebnis der Berechnung an.
- DEL-Button: Löscht das letzte Zeichen in der aktuellen Eingabe.
- Clear-Button: Löscht die gesamte Eingabe und den Verlauf.
- Verlauf: Zeigt die letzten 7 Berechnungen an.

Einschränkungen
Die Berechnungen werden mit der Python eval()-Funktion durchgeführt. Stelle sicher, dass nur valide mathematische Ausdrücke eingegeben werden.
Division durch Null und andere ungültige Ausdrücke führen zu einem Fehler und zeigen "Error" an.