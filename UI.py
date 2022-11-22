from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_create = QtWidgets.QPushButton(Form)
        self.btn_create.setMinimumSize(QtCore.QSize(196, 50))
        self.btn_create.setMaximumSize(QtCore.QSize(196, 50))
        self.btn_create.setObjectName("btn_create")
        self.gridLayout.addWidget(self.btn_create, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Bruh"))
        self.btn_create.setText(_translate("Form", "Нарисовать кружочек :)"))
