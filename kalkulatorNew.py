from PyQt6 import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import sys

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(600,600)
        mainWidget = QWidget()
        layout = QVBoxLayout()
        mainWidget.setLayout(layout)
        self.setCentralWidget(mainWidget)
        
        hLayout = QHBoxLayout()
        layout.addLayout(hLayout)
        self.wyswietlacz = QTextEdit(self)
        self.wyswietlacz.setText("0")
        self.wyswietlacz.setFixedSize(580,55)
        hLayout.addWidget(self.wyswietlacz)
        
        self.pamiec = []
        self.liczba = ""
        self.wynik = ""
        
        i = 1 
        hLayout = QHBoxLayout()
        rowWidget = QWidget()
        rowWidget.setLayout(hLayout)
        
        for column in range(3):
            button = self.CreateButton(str(i))
            hLayout.addWidget(button)
            i += 1
            if i == 4:
                button = self.CreateButton2("+")
                hLayout.addWidget(button)
            layout.addWidget(rowWidget)
        
        i = 4
        hLayout = QHBoxLayout()
        rowWidget = QWidget()
        rowWidget.setLayout(hLayout)
        for column in range(3):
            button = self.CreateButton(str(i))
            hLayout.addWidget(button)
            i += 1
            if i == 7:
                button = self.CreateButton2("-")
                hLayout.addWidget(button)
            layout.addWidget(rowWidget)
        
        i = 7
        hLayout = QHBoxLayout()
        rowWidget = QWidget()
        rowWidget.setLayout(hLayout)
        
        for column in range(3):
            button = self.CreateButton(str(i))
            hLayout.addWidget(button)
            i += 1
            if i == 10:
                button = self.CreateButton2("*")
                hLayout.addWidget(button)
            layout.addWidget(rowWidget)
            
        i = 10
        hLayout = QHBoxLayout()
        rowWidget = QWidget()
        rowWidget.setLayout(hLayout)
        
        for column in range(3):
            if i == 10:
                button = self.CreateButton(".")
                hLayout.addWidget(button)
                i += 1
            if i == 11:
                button = self.CreateButton("0")
                hLayout.addWidget(button)
                i += 1
            if i == 12:
                button = QPushButton()
                button.setText("=")
                button.setFixedSize(130,90)
                button.clicked.connect(lambda b: self.rownasie())
                hLayout.addWidget(button)
                i += 1
            if i == 13:
                button = self.CreateButton2("/")
                hLayout.addWidget(button)
                i +=1
            layout.addWidget(rowWidget)
            
        i = 13
        hLayout = QHBoxLayout()
        rowWidget = QWidget()
        rowWidget.setLayout(hLayout)
        
        for column in range(3):
            if i == 13:
                button = QPushButton()
                button.setText("C")
                button.setFixedSize(130,90)
                button.clicked.connect(lambda b: self.czyszczenie())
                hLayout.addWidget(button)
                i += 1
            if i == 14:
                button = QPushButton()
                button.setText("kasuj")
                button.setFixedSize(130,90)
                button.clicked.connect(lambda b: self.kasowanie())
                hLayout.addWidget(button)
                i += 1
            if i == 15:
                button = self.CreateButton2("^")
                hLayout.addWidget(button)
                i += 1
            if i == 16:
                button = self.CreateButton3(" ")
                hLayout.addWidget(button)
                i += 1
            layout.addWidget(rowWidget)
                   
    def CreateButton(self, text) -> QPushButton:
        button = QPushButton()
        button.setText(text)
        button.setFixedSize(130,90)
        button.clicked.connect(lambda b: self.onButtonClick(text))
        return button
    
    def CreateButton2(self, text) -> QPushButton:
        button = QPushButton()
        button.setText(text)
        button.setFixedSize(130,90)
        button.clicked.connect(lambda b: self.onButtonClick2(text))
        return button

    def CreateButton3(self, text) -> QPushButton:
        button = QPushButton()
        button.setText(text)
        button.setFixedSize(130,90)
        return button
    
    def onButtonClick(self, button: QPushButton):
        if len(self.pamiec) == 0:
            if button == '.':
                self.pamiec.append("0.")
                self.wyswietlacz.setText("0.")
            else:
                self.pamiec.append(button)
                self.wyswietlacz.setText(button)
        elif len(self.pamiec) == 1:
            if self.pamiec[0] == "0" and button != '.' :
                self.pamiec[0] = button
                self.wyswietlacz.setText(button)
            else:
                self.pamiec[0] += button
                self.wyswietlacz.setText(self.pamiec[0])
        if len(self.pamiec) == 2:
            if button == '.':
                self.pamiec.append("0.")
                self.wyswietlacz.setText("0.")
            else:
                self.pamiec.append(button)
                self.wyswietlacz.setText(button)
        elif len(self.pamiec) == 3:
            if self.pamiec[2] == "0" and button != '.' :
                self.pamiec[2] = button
                self.wyswietlacz.setText(button)
            else:
                self.pamiec[2] += button
                self.wyswietlacz.setText(self.pamiec[2])
        print(self.pamiec)
    
    def onButtonClick2(self, button: QPushButton):
        if len(self.pamiec) == 0:
            if self.wynik == "" :
                self.pamiec.append('0')
            else:
                self.pamiec.append(self.wynik)
            print(self.pamiec)
        if len(self.pamiec) == 1:
            self.pamiec.append(button)
            print(self.pamiec)
        elif len(self.pamiec) == 2:
            self.pamiec[1] = button
            print(self.pamiec)
        if len(self.pamiec) == 3:
            wynik = str(self.oblicz(float(self.pamiec[0]),self.pamiec[1],float(self.pamiec[2],)))
            if self.pamiec[1] == '/' and self.pamiec[2] == '0':
                self.wyswietlacz.setText("Nie mozna dzielic przez 0 !!!!")
                self.pamiec = []
            else:
                self.wyswietlacz.setText(wynik)
                self.pamiec = []
                self.pamiec.append(wynik)
                self.pamiec.append(button)
                print(self.pamiec)
            
    def czyszczenie(self):
        self.pamiec = []
        self.wyswietlacz.setText("0")
        
    def kasowanie(self):
        if len(self.pamiec) == 1:
            if len(self.pamiec[0]) == 1:
                self.pamiec = []
                self.wyswietlacz.setText('0')
            else:
                self.pamiec[0] = (self.pamiec[0])[:-1]
                self.wyswietlacz.setText(self.pamiec[0])
        if len(self.pamiec) == 3:
            if len(self.pamiec[2]) == 1:
                self.pamiec[2] = "0"
                self.wyswietlacz.setText('0')
            else:
                self.pamiec[2] = (self.pamiec[2])[:-1]
                self.wyswietlacz.setText(self.pamiec[2])
        pass
        print(self.pamiec)
        
    def rownasie(self):
        if len(self.pamiec) == 3:
            self.wynik = str(self.oblicz(float(self.pamiec[0]),self.pamiec[1],float(self.pamiec[2],)))
            if self.pamiec[1] == '/' and self.pamiec[2] == '0':
                self.wyswietlacz.setText("Nie mozna dzielic przez 0 !!!!")
                self.pamiec = []
            else:
                self.wyswietlacz.setText(self.wynik)
                self.pamiec = []
    
    def oblicz(self,*parametry):
        działania = {
        "+": lambda a,b : a+b, "-": lambda a,b : a - b,
        "*": lambda a,b : a*b , "/": lambda a,b : a/b,
        "^": lambda a,b : a**b,"%": lambda a,b : a%b,
        "root" : lambda a,b : a**(1/b)}
        operacja = parametry[1]
        a = parametry[0]
        b = parametry[2]
        wynik = działania[operacja]
        if operacja == "/" and b == 0:
            return "Nie mozna dzielic przez 0 !!!!"
        else:
            return wynik(a,b)
        
app = QApplication(sys.argv)

window = Main()
window.show()

app.exec()
