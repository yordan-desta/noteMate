from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from mainwindow import *
import thread
import time
import splash
class mainWindow(QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        self.wordCount=0
        super(mainWindow,self).__init__(parent)
        self.setupUi(self)
        #e= self.height()
        #self.resizeEvent()
        self.setFixedWidth(self.width())
        self.setFixedHeight(self.height())
        self.check_size(self)
        self.setGeometry(1000,0,342, 481)

        self.delButton.setText("<-")
        self.addButton.setText("+")
        self.saveButton.setText("save")
        self.textEdit.appendPlainText("")
        self.textEdit.setFocus()
        self.setWindowTitle("noteMate(test Release)")

    def startUpSetup(self):

        self.topicCombobox.addItems(self.topicList)
        for i,topics in enumerate(self.topicList):
            if topics==self.callerButId:
                self.topicCombobox.setCurrentIndex(i)
        #create if file not exist
        topic=self.topicCombobox.currentText()
        self.setupTopicWindow(topic)
        self.connect(self.delButton,SIGNAL("clicked()"),self.deleteCurrentTopic)
        self.connect(self.saveButton,SIGNAL("clicked()"),self.saveCurrentTopicText)
        self.connect(self.addButton,SIGNAL("clicked()"),self.backToSplash)
        self.connect(self.topicCombobox, SIGNAL("currentIndexChanged(QString)"),self.updateTextEdit)
        if len(self.topicList)==1:
            self.delButton.setEnabled(False)
        else:
            self.delButton.setEnabled(True)

    def saveCurrentTopicText(self):
        topic=self.topicCombobox.currentText()
        try:
            file=open(topic,'w')
            topicText=self.textEdit.toPlainText()
            file.write(topicText)
            """display saved msg and disable save button"""
            file.close()

        except:
            pass


    def check_size(self,x):
        print "resized"
        while self.windowState():
           self.textEdit.setFixedHeight(self.height())
           self.textEdit.setFixedWidth(self.width())


    def topicItems(self,topicList,callerButId):

        self.topicList= topicList
        self.callerButId=callerButId
        self.startUpSetup()

    def getTopicFileText(self,topic):

        try:
            file=open(topic,'r')
            text= file.read()
            file.close()
            return text

        except:
            return ValueError


    def backToSplash(self):
        self.sd=splash.splashDialog()
        self.sd.setupUI()
        self.sd.setModal(True)
        self.sd.show()
        #self.sd.exec_()
        self.hide()

    def updateTextEdit(self,currentTopic):
        #save previous textedit
        #self.saveCurrentTopicText()
        #cleanup edit text
        self.textEdit.clear()
        if len(self.topicList)>0:

            #show the text for current topic
            print len(self.topicList)
            self.setupTopicWindow(currentTopic)

    def setupTopicWindow(self,topic):
        for i,t in enumerate(self.topicList):
            if t==topic:
                self.topicCombobox.setCurrentIndex(i)
                break
        try:
            file=open(topic,'r')
            print "the file for %s exists"%(self.topicCombobox.currentText())
            file.close()
            topicText=self.getTopicFileText(topic)
            self.textEdit.setPlainText(topicText)
        except:
            file=open(topic,'w')
            print "the file for %s is created for the first time"%(self.topicCombobox.currentText())
            file.close()
    def deleteCurrentTopic(self):
        topic=self.topicCombobox.currentText()
        topicIndex=self.topicCombobox.currentIndex()
        self.deleteTopic(topic,topicIndex)
    def deleteTopic(self,topic,index=0):
        #delete from newWindow

        for i,t in enumerate(self.topicList):
            if t==topic and i==index:
                self.topicList.remove(topic)
                break

        #delete from splash List
        file=open("arrayList",'r')


        self.topicCombobox.removeItem(index)
        self.delFromSplash(topic)
        #self.topicCombobox.setCurrentIndex(index-1)
        #file=open(topic)
        #del file
        print len(self.topicList),self.topicList
        if(len(self.topicList)>0):

            topic=self.topicList[0]
            self.setupTopicWindow(topic)
            self.delButton.setEnabled(True)
        else:
            self.saveButton.setEnabled(False)
            self.topicCombobox.setEnabled(False)
            self.delButton.setEnabled(False)

        #self.startUpSetup()
        #print self.topicList
        #print self.callerButId

    def delFromSplash(self,topic):
        file=open("arrayList",'r')
        r=file.read()
        rs=r.split(",")
        file.close()
        file=open("arrayList",'w')
        for t in rs:
            if t==topic:
                continue
            if t=="":
                continue
            else:
                if t!=rs[::-1]:
                    file.write(t+",")
                else:
                    file.write(t)

        file.close()
