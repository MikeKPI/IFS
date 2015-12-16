import os
import sys

# For MainWindowUi relative import
sys.path.append(os.path.abspath(os.path.dirname(__name__)))

from PyQt5 import QtWidgets
from main_window_ui import Ui_Form as MainWindowUi


class MainWindow(QtWidgets.QWidget, MainWindowUi):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setup()
        self.show()

    def setup(self):
        self.pushButton.clicked.connect(self.draw_graphics)
        self.minus_btn.clicked.connect(self.scale_minux)
        self.plus_btn.clicked.connect(self.scale_plus)
        self.draw_graphics()

    def scale_plus(self):
        self.graphicsView.set_scale(2)

    def scale_minux(self):
        self.graphicsView.set_scale(0.5)

    def draw_graphics(self):
        x = self.start_x_ledit.text()
        y = self.start_y_ledit.text()
        num_iter = self.iter_num_ledit.text()
        if x is None:
            self.start_x_ledit.setText('Value not entered')
            return
        elif y is None:
            self.start_y_ledit.setText('Value not entered')
            return
        elif num_iter is None:
            self.iter_num_ledit.setText('Value not entered')
            return
        else:
            self.graphicsView.draw_all(int(x), int(y), int(num_iter))
