__author__ = 'pyordan'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


buttonArray=[]

class splashDialog(QDialog):
    def setupUI(self):
        self.topicCount=0

        self.vlayMain=QVBoxLayout()
        self.hlay=QHBoxLayout()
        self.qlable=QLabel("Select your topic")
        self.addbut=QPushButton("add")

        self.vlay=QVBoxLayout()

        self.hlay.addWidget(self.qlable)
        self.hlay.addWidget(self.addbut)

        self.vlayMain.addLayout(self.hlay)

        self.setLayout(self.vlayMain)

        self.setWindowTitle("noteMate")

        self.connect(self.addbut,SIGNAL("clicked()"),self.addTopic)

    def addTopic(self,topic="Topic"):
        self.topicCount+=1
        topBut=QPushButton()
        title=topic + " "+str(self.topicCount)
        topBut.setText(title)
        self.vlay.addWidget(topBut)
        self.vlayMain.addLayout(self.vlay)
        topBut.setObjectName("button" + str(self.topicCount))
        buttonArray.append(topBut.objectName())
        for name in buttonArray:
            print name

