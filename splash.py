__author__ = 'pyordan'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
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

        self.hlay.addWidget(self.qlable)
        self.hlay.addWidget(self.addbut)

        self.vlayMain.addLayout(self.hlay)

        self.setLayout(self.vlayMain)

        self.setWindowTitle("noteMate")

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
                self.vlay.addWidget(topBut)
                self.vlayMain.addLayout(self.vlay)

                if topBut in buttonArray:
                    continue

                topBut.setObjectName(topic)

                buttonArray.append(topBut)
        for i,t in enumerate(topics):
            if t=="":
                #print "empty"
                del topics[i]
        print "*****",topics,"*****"
        self.saveTopics()
        for i,objectname in enumerate(buttonArray):

            self.connect(objectname,SIGNAL("topic_clicked(QString)"),self.startwindow)
        self.countForAddtopicEntry+=1
    def addButtonClicked(self):
        self.addButtonIsClicked=True
       # print self.addButtonIsClicked
        self.atui=addTopicUi()
        self.hide()
        self.atui.setupUi()

    def startwindow(self,buttonObjName):
        #print buttonObjName
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
                    #print topic
                file.close()
                #print topics
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
           # print topic
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
        self.setWindowTitle("Title")
        self.show()
        self.connect(self.okbut,SIGNAL("clicked()"),self.addtopic)
    def addtopic(self):
        global topicTitle,topicIsAdded,topics
        #print topicIsAdded
        global savedTopics
        savedTopics=True
        topicTitle=self.line.text()
        topicIsAdded=True
        #print topicTitle
        self.sd=splashDialog()
        self.sd.setupUI()
        self.hide()
        self.sd.show()
        #self.sd.exec_()


class topicButtons(QPushButton):
    def __init__(self,parent=None):
        super(topicButtons,self).__init__(parent)
        self.connect(self,SIGNAL("clicked()"),self.topicClicked)

    def topicClicked(self):
        self.objName=str(self.objectName())
        #print type(self.objName)
        self.emit(SIGNAL("topic_clicked(QString)"),self.objName)
