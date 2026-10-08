import random
from maya import cmds
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLineEdit,
    QLabel,
    QPushButton,
    QGridLayout,
    QVBoxLayout,
    QHBoxLayout
)

from PySide6 import QtCore

class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 4-5")
        self.setMinimumWidth(400)
        self.build_ui()
    
    def build_ui(self):
        layout = QGridLayout(self)


        label_number_objects = QLabel("Number of objects")
        layout.addWidget(label_number_objects, 0, 0)
        self.text_input_number_objects = QLineEdit()
        layout.addWidget(self.text_input_number_objects, 0, 1)

        label_min = QLabel("Min")
        layout.addWidget(label_min, 1, 1)
        

        label_max = QLabel("Max")
        layout.addWidget(label_max, 1, 2)
        

        label_posx = QLabel("Position X")
        layout.addWidget(label_posx, 2, 0)
        self.text_input_posx_min = QLineEdit()
        layout.addWidget(self.text_input_posx_min, 2, 1)
        self.text_input_posx_max = QLineEdit()
        layout.addWidget(self.text_input_posx_max, 2, 2)

        label_posy = QLabel("Position Y")
        layout.addWidget(label_posy, 3, 0)
        self.text_input_posy_min = QLineEdit()
        layout.addWidget(self.text_input_posy_min, 3, 1)
        self.text_input_posy_max = QLineEdit()
        layout.addWidget(self.text_input_posy_max, 3, 2)

        label_posz = QLabel("Position Z")
        layout.addWidget(label_posz, 4, 0)
        self.text_input_posz_min = QLineEdit()
        layout.addWidget(self.text_input_posz_min, 4, 1)
        self.text_input_posz_max = QLineEdit()
        layout.addWidget(self.text_input_posz_max, 4, 2)

        label_scale = QLabel("Scale")
        layout.addWidget(label_scale, 5, 0)
        self.text_input_scale_min = QLineEdit()
        layout.addWidget(self.text_input_scale_min, 5, 1)
        self.text_input_scale_max = QLineEdit()
        layout.addWidget(self.text_input_scale_max, 5, 2)

        self.create_button = QPushButton("Create objects")
        self.create_button.clicked.connect(self.create_object)
        layout.addWidget(self.create_button, 6, 0, 1, 3)

    
        

    def create_object(self):
        forme = random.choice(["cube", "cylindre", "sphere"])

        if forme == "cube":
            objet = cmds.polyCube()[0]
        elif forme == "cylindre":
            objet = cmds.polyCylinder()[0]
        else:
            objet = cmds.polySphere()[0]

        random_value = random.uniform(-10, 10)
        cmds.move(random_value, random_value, random_value, objet)


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()