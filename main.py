import sys
import random as rnd
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPointF
from PyQt5 import uic
from UI import *


class Widget(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        QWidget.__init__(self)
        self.setupUi(self)
        self.start_drawing = False
        self.btn_create.clicked.connect(self.draw)
        
    def draw(self, event):
        self.start_drawing = True
        self.update()

    def paintEvent(self, event):
        if self.start_drawing:
            qp = QPainter()	
            qp.begin(self)
            
            qp.setBrush(QColor(rnd.randint(0, 255), 
                               rnd.randint(0, 255),
                               rnd.randint(0, 255)))
            pos = QPointF(rnd.uniform(100, 700), rnd.uniform(100, 500))
            radius = rnd.uniform(25, 250)
            qp.drawEllipse(pos, radius, radius)
            
            qp.end()
            self.start_drawing = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    app.exec_()
