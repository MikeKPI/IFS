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
        self.show()
