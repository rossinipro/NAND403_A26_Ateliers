import random
from maya import cmds
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLineEdit,
    QLabel,
    QPushButton,
    QGridLayout,
)

from PySide6 import QtCore

class FenceGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 6")
        self.setMinimumWidth(400)
        self.build_ui()
    
    def build_ui(self):
        layout = QGridLayout(self)

        # Number of posts
        label_number_posts = QLabel("How many posts?")
        layout.addWidget(label_number_posts, 1, 0)
        self.text_input_number_posts = QLineEdit()
        layout.addWidget(self.text_input_number_posts, 1, 1)

        #number of frames
        label_number_frames = QLabel("How many frames?")
        layout.addWidget(label_number_frames, 2, 0)
        self.text_input_number_frames = QLineEdit()
        layout.addWidget(self.text_input_number_frames, 2, 1)


        label_posx = QLabel("Profondeur")
        layout.addWidget(label_posx, 3, 1)
        label_posy = QLabel("Hauteur")
        layout.addWidget(label_posy, 3, 2)
        label_posz = QLabel("Largeur")
        layout.addWidget(label_posz, 3, 3)


        label_scale = QLabel("Scale")
        layout.addWidget(label_scale, 5, 0)
        self.text_input_scaleX = QLineEdit()
        layout.addWidget(self.text_input_scaleX, 5, 1)
        self.text_input_scaleY = QLineEdit()
        layout.addWidget(self.text_input_scaleY, 5, 2)
        self.text_input_scaleZ = QLineEdit()
        layout.addWidget(self.text_input_scaleZ, 5, 3)

        #add an empty line for spacing
        layout.addWidget(QLabel(""), 6, 0) 


        #distance between posts
        label_distance = QLabel("Distance between posts")
        layout.addWidget(label_distance, 7, 0)
        self.text_input_distance = QLineEdit()
        layout.addWidget(self.text_input_distance, 7, 1)

        # Create button
        self.create_button = QPushButton("Create fence")
        self.create_button.clicked.connect(self.create_fence)
        layout.addWidget(self.create_button, 10, 0, 1, 3)

    
        

    def create_fence(self):
        cmds.undoInfo(chunkName='renameChunk', openChunk=True)

        # Get the number of objects to create
        number_posts = int(self.text_input_number_posts.text())
        number_frames = int(self.text_input_number_frames.text())

        # Get the values for scale
        scaleX = float(self.text_input_scaleX.text())
        scaleY = float(self.text_input_scaleY.text())
        scaleZ = float(self.text_input_scaleZ.text())

        # Get the distance between posts
        distance = float(self.text_input_distance.text())

        for i in range(number_posts):

            # Create the post
            post = cmds.polyCube()[0]
            cmds.scale(scaleX, scaleY, scaleZ, post)
            cmds.move(i * distance, scaleY/2, 0, post)
            cmds.rename(post, f'Post_{i}')

            #create the frames between the posts
            if i < number_posts - 1: #stop creating frames after the last post
                for j in range(number_frames):
                    frame = cmds.polyCube()[0]
                    cmds.scale((scaleX + distance) - scaleX/2, 1, scaleZ/2, frame)
                    cmds.move((i * distance) + distance/2, ((j * (scaleY / number_frames)) + .5), 0, frame)
                    cmds.rename(frame, f'Frame_{i}_{j}')

        cmds.undoInfo(chunkName='renameChunk', closeChunk=True) 

def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = FenceGenerator()
    tool_window.show()

main()