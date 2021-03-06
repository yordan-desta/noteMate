__author__ = 'pyordan'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

try:
    _fromUtf8 =QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

from newWindow import *
buttonArray=[]
topicTitle=""
topicIsAdded=False
topics=[]
selfinitFlag=True
savedTopics=True
class splashDialog(QDialog):
    def setupUI(self):
        self.initTopics()
        self.countForAddtopicEntry=0
        self.addButtonIsClicked=False
        self.topicCount=0
        global topics,topicIsAdded,topicTitle,buttonArray,savedTopics
        self.vlayMain=QVBoxLayout()
        self.hlay=QHBoxLayout()
        self.qlable=QLabel("Select your topic")
        self.addbut=QPushButton("add")
        self.vlay=QVBoxLayout()
        self.setWindowTitle("noteMate V0.2")
        self.hlay.addWidget(self.qlable)
        self.hlay.addWidget(self.addbut)
        self.vlayMain.addLayout(self.hlay)
        self.setLayout(self.vlayMain)
        if savedTopics and (len(topics)!=0 or (topicIsAdded and topicTitle!="")):
            topicIsAdded=False
            self.addTopic(topicTitle)
            topicTitle=""

        self.connect(self.addbut,SIGNAL("clicked()"),self.addButtonClicked)

    def addTopic(self,topictitle="Topic"):
        """resetting button array list"""
        buttonArray=[]
        topics.append(topictitle)
        for topic in topics:
            if topic!="":
                topBut=topicButtons()
                topBut.setText(topic)
                topBut.setStyleSheet(_fromUtf8("color: rgb(0, 85, 255);\n"
"font: 75 9pt \"Microsoft JhengHei UI\";\n"
""))
                self.vlay.addWidget(topBut)
                self.vlayMain.addLayout(self.vlay)

                if topBut in buttonArray:
                    continue

                topBut.setObjectName(topic)

                buttonArray.append(topBut)
        for i,t in enumerate(topics):
            if t=="":
                del topics[i]

        self.saveTopics()
        for i,objectname in enumerate(buttonArray):

            self.connect(objectname,SIGNAL("topic_clicked(QString)"),self.startwindow)
        self.countForAddtopicEntry+=1
    def addButtonClicked(self):
        self.addButtonIsClicked=True
        self.atui=addTopicUi()
        self.hide()
        self.atui.setupUi()
    def startwindow(self,buttonObjName):
        self.nw= mainWindow()
        self.nw.topicItems(topics,buttonObjName)
        self.nw.show()
        self.hide()
    """save and restore lists"""
    def initTopics(self):
        if selfinitFlag:
            global topics
            try:
                file=open("arrayList",'r')
                read=file.read()
                rtopics=read.split(",")
                """check is there is any saved topics"""
                if len(rtopics)==1 and rtopics[0]=='':
                    global savedTopics
                    savedTopics=False
                for topic in rtopics:
                 topics.append(topic)
                 file.close()
                self.saveTopics()
            except:
                file=open("arrayList",'w+')
            file.close()
            global selfinitFlag
            selfinitFlag=False
    def saveTopics(self):
        file=open("arrayList",'w+')
        count=0
        for topic in topics:
            if count==0:
                file.write(topic)
                count+=1
            else:
                file.write(","+topic)
        file.close()
class addTopicUi(QDialog):
    def setupUi(self):
        self.hlay=QHBoxLayout()
        self.line=QLineEdit()
        self.okbut=QPushButton("ok")
        self.hlay.addWidget(self.line)
        self.hlay.addWidget(self.okbut)
        self.setLayout(self.hlay)
        self.setWindowTitle("")
        self.setWindowFlags(Qt.SplashScreen)
        self.show()

        self.connect(self.okbut,SIGNAL("clicked()"),self.addtopic)
    def addtopic(self):
        global topicTitle,topicIsAdded,topics
        global savedTopics
        savedTopics=True
        topicTitle=self.line.text()
        topicIsAdded=True
        self.sd=splashDialog()
        self.sd.setupUI()
        self.hide()
        self.sd.show()

class topicButtons(QPushButton):
    def __init__(self,parent=None):
        super(topicButtons,self).__init__(parent)
        self.connect(self,SIGNAL("clicked()"),self.topicClicked)
    def topicClicked(self):
        self.objName=str(self.objectName())
        self.emit(SIGNAL("topic_clicked(QString)"),self.objName)
