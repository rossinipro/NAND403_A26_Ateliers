from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QSpinBox,
    QDoubleSpinBox,
    QPushButton,
    QMessageBox
)
from PySide6.QtCore import Qt
import random

from maya import cmds
import maya.OpenMayaUI as omui
from shiboken6 import wrapInstance #used to access information of C++

def maya_main_window():
    pointer = omui.MQtUtil.mainWindow() #open maya main window
    return wrapInstance(int(pointer), QWidget) #wraps the pointer to a QWidget

class Scatter(QWidget):
    def __init__(self):
        super().__init__(maya_main_window()) #add the maya main window as the parent of this widget, so it doesnt get lost in the background
        self.setWindowFlags(Qt.Window)
        self.build_ui()
        
    def build_ui(self):
        layout = QVBoxLayout(self)
        form = QFormLayout()
        layout.addLayout(form)

        self.count_spin = QSpinBox()
        self.count_spin.setRange(1, 100)
        self.count_spin.setValue(10)
        self.count_spin.valueChanged.connect(self.apply_scatter) #live update
        form.addRow("Copies", self.count_spin)

        self.radius_spin = QDoubleSpinBox()
        self.radius_spin.setRange(1.0, 50.0)
        self.radius_spin.setValue(10.0)
        self.radius_spin.valueChanged.connect(self.apply_scatter) #live update
        form.addRow("Radius", self.radius_spin)

        self.seed_spin = QSpinBox()
        self.seed_spin.setRange(0, 9999)
        self.seed_spin.valueChanged.connect(self.apply_scatter) #live update
        form.addRow("Seed", self.seed_spin)

        scatter_button = QPushButton("Scatter")
        scatter_button.clicked.connect(self.apply_scatter)
        layout.addWidget(scatter_button)

 
    def apply_scatter(self):
        cmds.undo() #undo anything that was done before making it again
        selection = cmds.ls(selection=True, transforms=True)
        if not selection:
            QMessageBox.warning(self, "Scatter", "Select an object first.")
            return
        source = selection[0]

        cmds.undoInfo(openChunk=True)
        try:
            random.seed(self.seed_spin.value())
            radius = self.radius_spin.value()
            group = cmds.group(empty=True, name="scatter_grp")
            for i in range(self.count_spin.value()):
                copy = cmds.duplicate(source)[0]
                copy = cmds.parent(copy, group)[0]
                x = random.uniform(-radius, radius)
                z = random.uniform(-radius, radius)
                cmds.move(x, 0, z, copy, relative=True)
        finally:
            cmds.undoInfo(closeChunk=True)
 
def show_scatter():
    global scatter
    try:
        scatter.close()
    except:
        pass
    scatter = Scatter()
    scatter.show()
 
show_scatter()   