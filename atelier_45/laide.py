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

        # Number of objects input
        label_number_objects = QLabel("Number of objects")
        layout.addWidget(label_number_objects, 0, 0)
        self.text_input_number_objects = QLineEdit()
        layout.addWidget(self.text_input_number_objects, 0, 1)

        label_min = QLabel("Min")
        layout.addWidget(label_min, 1, 1)
        

        label_max = QLabel("Max")
        layout.addWidget(label_max, 1, 2)
        
        # Position inputs
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

        # Create button
        self.create_button = QPushButton("Create objects")
        self.create_button.clicked.connect(self.create_object)
        layout.addWidget(self.create_button, 6, 0, 1, 3)

    
        

    def create_object(self):
        
        # Get the number of objects to create
        number_objects = int(self.text_input_number_objects.text())

        # Get the min and max values for position and scale
        posx_min = float(self.text_input_posx_min.text())
        posx_max = float(self.text_input_posx_max.text())
        posy_min = float(self.text_input_posy_min.text())
        posy_max = float(self.text_input_posy_max.text())
        posz_min = float(self.text_input_posz_min.text())
        posz_max = float(self.text_input_posz_max.text())
        scale_min = float(self.text_input_scale_min.text())
        scale_max = float(self.text_input_scale_max.text())

        # Create the specified number of objects
        for number in range(number_objects):
            
            #Choose a random shape for each object
            forme = random.choice(["cube", "cylindre", "sphere"])

            if forme == "cube":
                objet = cmds.polyCube()[0]
            elif forme == "cylindre":
                objet = cmds.polyCylinder()[0]
            else:
                objet = cmds.polySphere()[0]

            # Set random position and scale for each object
            random_posx = random.uniform(posx_min, posx_max)
            random_posy = random.uniform(posy_min, posy_max)
            random_posz = random.uniform(posz_min, posz_max)
            cmds.move(random_posx, random_posy, random_posz, objet)


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()