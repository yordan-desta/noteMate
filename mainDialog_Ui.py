# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainDialog_Ui.ui'
#
# Created: Fri Mar 13 14:37:56 2015
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

class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName(_fromUtf8("mainDialog"))
        mainDialog.resize(400, 300)
        mainDialog.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.d1AddButton = QtGui.QPushButton(mainDialog)
        self.d1AddButton.setGeometry(QtCore.QRect(300, 10, 98, 27))
        self.d1AddButton.setDefault(False)
        self.d1AddButton.setFlat(False)
        self.d1AddButton.setObjectName(_fromUtf8("d1AddButton"))
        self.d1Title = QtGui.QLabel(mainDialog)
        self.d1Title.setGeometry(QtCore.QRect(0, 10, 291, 31))
        self.d1Title.setAlignment(QtCore.Qt.AlignCenter)
        self.d1Title.setObjectName(_fromUtf8("d1Title"))
        self.scrollArea = QtGui.QScrollArea(mainDialog)
        self.scrollArea.setGeometry(QtCore.QRect(9, 49, 381, 241))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 379, 239))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)

    def retranslateUi(self, mainDialog):
        mainDialog.setWindowTitle(_translate("mainDialog", "Dialog", None))
        self.d1AddButton.setText(_translate("mainDialog", "Add", None))
        self.d1Title.setText(_translate("mainDialog", "Choose your topic", None))


