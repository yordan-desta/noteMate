# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created: Tue Mar 24 11:38:06 2015
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
        self.topicCombobox = QtGui.QComboBox(Dialog)
        self.topicCombobox.setGeometry(QtCore.QRect(40, 2, 261, 26))
        self.topicCombobox.setObjectName(_fromUtf8("topicCombobox"))
        self.addButton = QtGui.QPushButton(Dialog)
        self.addButton.setGeometry(QtCore.QRect(306, 2, 31, 26))
        self.addButton.setText(_fromUtf8(""))
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.delButton = QtGui.QPushButton(Dialog)
        self.delButton.setGeometry(QtCore.QRect(3, 2, 31, 26))
        self.delButton.setText(_fromUtf8(""))
        self.delButton.setObjectName(_fromUtf8("delButton"))
        self.textEdit = QtGui.QPlainTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(4, 30, 337, 451))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.saveButton = QtGui.QPushButton(Dialog)
        self.saveButton.setGeometry(QtCore.QRect(301, 450, 35, 27))
        self.saveButton.setText(_fromUtf8(""))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.saveButton, self.addButton)
        Dialog.setTabOrder(self.addButton, self.topicCombobox)
        Dialog.setTabOrder(self.topicCombobox, self.textEdit)
        Dialog.setTabOrder(self.textEdit, self.delButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))

