#/usr/bin/env python3.5

import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow

app = QApplication(sys.argv)
gui = MainWindow()

sys.exit(app.exec_())
