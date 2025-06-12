# Form implementation generated from reading ui file 'pengaduan.ui'
# Created manually (simulating pyuic6 output)
from PyQt6 import QtCore, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.label = QtWidgets.QLabel(Form)
        self.label.setText("Tulis Pesan Pengaduan:")
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.verticalLayout.addWidget(self.textEdit)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setText("Kirim Aduan")
        self.verticalLayout.addWidget(self.pushButton)
        QtCore.QMetaObject.connectSlotsByName(Form)
