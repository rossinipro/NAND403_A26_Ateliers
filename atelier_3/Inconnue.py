# venv (pathtopython -m venv .venv) <- for python in general

#maya used mel before python
#script editor for code
#ctrl + enter to try code in maya 

#----- configure vscode for maya
#1-open extension on vscode (maya python)
#2-change interpreter to mayapy.exe (inside maya files/bin)
#3- ctrl-enter, go to maya, open script editor and run code there
#always save before running

import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QMessageBox, QApplication, QLineEdit, QPushButton

 
class MessageBoard(QWidget): 
    def __init__(self): #constructeur
        super().__init__()  #constructeur Qwidget
        self.setWindowTitle("Message board")
        self.setFixedSize(500,200)
        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Enter something here:")
        layout.addWidget(label)
        
        #textedit
        self.text_input = QLineEdit()
        layout.addWidget(self.text_input)
        

        #pushbuttom
        self.button = QPushButton('Print', self)        
        self.button.clicked.connect(self.button_onClicked)
        layout.addWidget(self.button)


        self.setLayout(layout)

    def button_onClicked(self):
        text_print = self.text_input.text()
        print (text_print)

    

    


 
def main():
    
    global widget
    widget = MessageBoard()
    widget.show()
 
main()