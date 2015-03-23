# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Mar 23 20:02:29 2015
#      by: PyQt4 UI code generator 4.10.4
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
        self.topicCombobox.setGeometry(QtCore.QRect(30, 0, 281, 27))
        self.topicCombobox.setObjectName(_fromUtf8("topicCombobox"))
        self.addButton = QtGui.QPushButton(Dialog)
        self.addButton.setGeometry(QtCore.QRect(310, 0, 31, 27))
        self.addButton.setText(_fromUtf8(""))
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.delButton = QtGui.QPushButton(Dialog)
        self.delButton.setGeometry(QtCore.QRect(0, 0, 31, 27))
        self.delButton.setText(_fromUtf8(""))
        self.delButton.setObjectName(_fromUtf8("delButton"))
        self.textEdit = QtGui.QPlainTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(0, 30, 341, 451))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.saveButton = QtGui.QPushButton(Dialog)
        self.saveButton.setGeometry(QtCore.QRect(300, 450, 31, 27))
        self.saveButton.setText(_fromUtf8(""))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.topicCombobox, self.addButton)
        Dialog.setTabOrder(self.addButton, self.saveButton)
        Dialog.setTabOrder(self.saveButton, self.textEdit)
        Dialog.setTabOrder(self.textEdit, self.delButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))

