from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from Taschenrechner_ui import Ui_MainWindow

class Hauptfenster(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.aktueller_text = ""
        self.verlauf = []
        
        validator = QRegExpValidator(QRegExp("[0-9\+\-\*/\(\)\,\s]*"))
        self.lineEdit_Rechnung.setValidator(validator)
        
        self.pushButton_Berechnen.clicked.connect(self.berechnen)
        self.pushButton_Clear.clicked.connect(self.clear)
        self.pushButton_DEL.clicked.connect(self.delete_last)
   
        self.lineEdit_Rechnung.returnPressed.connect(self.berechnen)
       
        self.show()
    
    def berechnen(self):      
        self.aktueller_text = self.lineEdit_Rechnung.text()
        try:
            ergebnis = str(eval(self.aktueller_text))
            self.lcdNumber.display(ergebnis)
            self.speichere_verlauf(f"{self.aktueller_text} = {ergebnis}")
            self.lineEdit_Rechnung.setText(ergebnis)
        except:
            self.lineEdit_Rechnung.setText("Error")
        
    def clear(self):
        self.aktueller_text = ""
        self.lcdNumber.display(0)
        self.lineEdit_Rechnung.clear()
        self.verlauf.clear()
        self.zeige_verlauf()
        
    def delete_last(self):   
        self.aktueller_text = self.lineEdit_Rechnung.text()
        self.aktueller_text = self.aktueller_text[:-1]
        self.lineEdit_Rechnung.setText(self.aktueller_text)
        self.lcdNumber.display(0)
    
    def speichere_verlauf(self, rechnung):
        if len(self.verlauf) >= 7:
            self.verlauf.pop(0)
        self.verlauf.append(rechnung)
        self.zeige_verlauf()
    
    def zeige_verlauf(self):
        for i, lineEdit in enumerate([
                self.lineEdit_Verlauf_1, self.lineEdit_Verlauf_2, self.lineEdit_Verlauf_3,
                self.lineEdit_Verlauf_4, self.lineEdit_Verlauf_5, self.lineEdit_Verlauf_6,
                self.lineEdit_Verlauf_7
            ]):
                if i < len(self.verlauf):
                    lineEdit.setText(self.verlauf[i])
                else:
                    lineEdit.clear()
                

         
app = QApplication ([])

fenster = Hauptfenster()

app.exec()