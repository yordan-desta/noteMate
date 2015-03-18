__author__ = 'pyordan'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from newWindow import *

buttonArray=[]
topicTitle=""
topicIsAdded=False
topics=[]
class splashDialog(QDialog):
    def setupUI(self):
        print "started splashDialog class"
        self.addButtonIsClicked=False
        self.topicCount=0

        global topics,topicIsAdded,topicTitle,buttonArray

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

        if len(topics)!=0 or (topicIsAdded and topicTitle!=""):
            print "topic title is "+topicTitle
            topicIsAdded=False
            self.addTopic(topicTitle)
            topicTitle=""

        #self.connect(self.addbut,SIGNAL("clicked()"),self.addButtonClicked)
        self.connect(self.addbut,SIGNAL("clicked()"),self.startwindow)

    def addTopic(self,topictitle="Topic"):
        print "title in addtopic is "+topictitle
        print "title in topics are "+str(topics)

        topics.append(topictitle)
        for topic in topics:
            if topic=="":
                topics.remove(topic)
                continue
            topBut=QPushButton()
            topBut.setText(topic)
            self.vlay.addWidget(topBut)
            self.vlayMain.addLayout(self.vlay)
            if topic in buttonArray:
                continue

            topBut.setObjectName(topic)
            buttonArray.append(topBut.objectName())
        for objectname in buttonArray:
            print objectname


        """
        topBut.setObjectName("button" + str(self.topicCount))
        buttonArray.append(topBut.objectName())
        """
    def addButtonClicked(self):
        self.addButtonIsClicked=True
        print "add button is clicked from splash.py"
        print self.addButtonIsClicked
        self.atui=addTopicUi()
        self.hide()
        self.atui.setupUi()

        #return self.addButtonIsClicked

    def startwindow(self):
        self.nw= mainWindow()
        self.nw.show()
        self.hide()

class addTopicUi(QDialog):
    def setupUi(self):
        self.hlay=QHBoxLayout()
        self.line=QLineEdit()
        self.okbut=QPushButton("ok")
        self.hlay.addWidget(self.line)
        self.hlay.addWidget(self.okbut)
        self.setLayout(self.hlay)
        self.setWindowTitle("Title")
        self.show()
        self.connect(self.okbut,SIGNAL("clicked()"),self.addtopic)
    def addtopic(self):
        global topicTitle,topicIsAdded,topics
        print topicIsAdded
        topicTitle=self.line.text()
        topicIsAdded=True
        print topicTitle
        self.sd=splashDialog()
        self.sd.setupUI()
        self.hide()
        self.sd.show()
        #self.sd.exec_()


