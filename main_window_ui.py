# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.iter_num_ledit = QtWidgets.QLineEdit(self.groupBox)
        self.iter_num_ledit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iter_num_ledit.sizePolicy().hasHeightForWidth())
        self.iter_num_ledit.setSizePolicy(sizePolicy)
        self.iter_num_ledit.setObjectName("iter_num_ledit")
        self.verticalLayout_2.addWidget(self.iter_num_ledit)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.start_x_ledit = QtWidgets.QLineEdit(self.groupBox)
        self.start_x_ledit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_x_ledit.sizePolicy().hasHeightForWidth())
        self.start_x_ledit.setSizePolicy(sizePolicy)
        self.start_x_ledit.setObjectName("start_x_ledit")
        self.verticalLayout_2.addWidget(self.start_x_ledit)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.start_y_ledit = QtWidgets.QLineEdit(self.groupBox)
        self.start_y_ledit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_y_ledit.sizePolicy().hasHeightForWidth())
        self.start_y_ledit.setSizePolicy(sizePolicy)
        self.start_y_ledit.setObjectName("start_y_ledit")
        self.verticalLayout_2.addWidget(self.start_y_ledit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addWidget(self.groupBox, 0, 1, 1, 1)
        self.graphicsView = DrawBoard(Form)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Fractal Parameters"))
        self.label.setText(_translate("Form", "Max iteration"))
        self.label_2.setText(_translate("Form", "Start X"))
        self.label_3.setText(_translate("Form", "Start Y"))
        self.pushButton.setText(_translate("Form", "Build"))

from drawboard import DrawBoard
