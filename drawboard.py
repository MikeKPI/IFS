from PyQt5 import QtWidgets


class DrawBoard(QtWidgets.QGraphicsView):

    def __init__(self, *args, **kwargs):
        super(DrawBoard, self).__init__(*args, **kwargs)
