# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created: Tue Mar 24 12:10:41 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(343, 481)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet(_fromUtf8(""))
        self.topicCombobox = QtGui.QComboBox(Dialog)
        self.topicCombobox.setGeometry(QtCore.QRect(40, 2, 261, 26))
        self.topicCombobox.setStyleSheet(_fromUtf8("color: rgb(0, 85, 255);\n"
"font: 75 9pt \"Microsoft JhengHei UI\";\n"
""))
        self.topicCombobox.setObjectName(_fromUtf8("topicCombobox"))
        self.addButton = QtGui.QPushButton(Dialog)
        self.addButton.setGeometry(QtCore.QRect(306, 2, 31, 26))
        self.addButton.setStyleSheet(_fromUtf8("color: rgb(42, 42, 255);\n"
""))
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.delButton = QtGui.QPushButton(Dialog)
        self.delButton.setGeometry(QtCore.QRect(3, 2, 31, 26))
        self.delButton.setStyleSheet(_fromUtf8("color: rgb(203, 5, 5);"))
        self.delButton.setObjectName(_fromUtf8("delButton"))
        self.textEdit = QtGui.QPlainTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(4, 30, 337, 451))
        self.textEdit.setStyleSheet(_fromUtf8("font: italic 12pt \"MS Sans Serif\";\n"
"background-color: rgb(255, 246, 107);"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.saveButton = QtGui.QPushButton(Dialog)
        self.saveButton.setGeometry(QtCore.QRect(301, 450, 35, 27))
        self.saveButton.setStyleSheet(_fromUtf8("font: italic 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 85, 255);"))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.saveButton, self.addButton)
        Dialog.setTabOrder(self.addButton, self.topicCombobox)
        Dialog.setTabOrder(self.topicCombobox, self.textEdit)
        Dialog.setTabOrder(self.textEdit, self.delButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.addButton.setText(_translate("Dialog", "+", None))
        self.delButton.setText(_translate("Dialog", "-", None))
        self.saveButton.setText(_translate("Dialog", "save", None))

