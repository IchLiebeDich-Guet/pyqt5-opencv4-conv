# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def __init__(self):
        self.label_6 = None
        self.pushButton_2 = None
        self.label_5 = None
        self.tableView = None
        self.label_4 = None
        self.label_3 = None
        self.label_2 = None
        self.comboBox = None
        self.lineEdit_2 = None
        self.pushButton = None
        self.label = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1092, 860)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 80, 121, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 470, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 470, 271, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(220, 80, 87, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(640, 70, 361, 361))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(640, 430, 361, 361))
        self.label_3.setObjectName("label_3")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(220, 140, 141, 151))
        self.tableView.setObjectName("tableView")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(510, 240, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(500, 600, 81, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 330, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 191, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "劣质卷积器"))
        self.label.setText(_translate("Form", "自动填充卷积核："))
        self.pushButton.setText(_translate("Form", "选择图片文件"))
        self.label_2.setText(_translate("Form", "原始图片"))
        self.label_3.setText(_translate("Form", "卷积后图片"))
        self.label_4.setText(_translate("Form", "原始图片："))
        self.label_5.setText(_translate("Form", "卷积后图片："))
        self.pushButton_2.setText(_translate("Form", "进行卷积"))
        self.label_6.setText(_translate("Form", "卷积核数值（可手动修改）："))