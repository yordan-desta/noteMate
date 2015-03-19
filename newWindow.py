from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from mainwindow import *
import thread
import time

class mainWindow(QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        super(mainWindow,self).__init__(parent)
        self.setupUi(self)
        #e= self.height()
        #self.resizeEvent()
        self.setFixedWidth(self.width())
        self.setFixedHeight(self.height())
        self.check_size(self)
        #self.connect(self.textEdit,SIGNAL("resizeEvent()"),self.check_size)
        #self.setMaximumHeight(658)
        #thread.start_new_thread(self.check_size,(e,))


        self.delButton.setText("-")
        self.addButton.setText("+")

    def check_size(self,x):
        print "resized"
        while self.windowState():
           self.textEdit.setFixedHeight(self.height())
           self.textEdit.setFixedWidth(self.width())

    def topicItems(self,topicList,callerButId):
        print callerButId
        print topicList
        """
        self.topicList=[]
        self.topicList.append("topic1")
        self.topicList.append("topic2")
        self.topicList.append("topic3")
        """
        self.topic= topicList
        self.topicCombobox.addItems(topicList)
