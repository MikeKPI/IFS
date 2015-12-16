from random import random
from PyQt5 import QtWidgets, QtGui, QtCore
from coral import coral_params, update_xy


class DrawBoard(QtWidgets.QGraphicsView):

    def __init__(self, *args, **kwargs):
        super(DrawBoard, self).__init__(*args, **kwargs)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scale_param = 3

    def set_scale(self, delta=0):
        self.scale_param = delta
        self.scale(self.scale_param, self.scale_param)

    def draw_all(self, x, y, num_iter):
        self.scene.clear()
        rad = 1.0
        pen = QtGui.QPen(QtCore.Qt.black)
        for _ in range(num_iter):
            x, y = update_xy(x, y, random(), coral_params)
            _x, _y = 10*x, 10*y
            self.scene.addEllipse(_x-rad, _y-rad, rad*0.5, rad*0.5,
                                  pen, QtGui.QBrush(QtCore.Qt.SolidPattern))
        self.setScene(self.scene)
