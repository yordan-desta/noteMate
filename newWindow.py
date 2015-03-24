from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
from mainwindow import *
import splash
class mainWindow(QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        self.wordCount=0
        super(mainWindow,self).__init__(parent)
        self.setupUi(self)
        self.setFixedWidth(self.width())
        self.setFixedHeight(self.height())
        self.check_size(self)
        self.setGeometry(1000,100,342, 481)
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
        topic=self.topicCombobox.currentText()
        self.setupTopicWindow(topic)
        self.connect(self.delButton,SIGNAL("clicked()"),self.deleteCurrentTopic)
        self.connect(self.saveButton,SIGNAL("clicked()"),self.saveCurrentTopicText)
        self.connect(self.addButton,SIGNAL("clicked()"),self.backToSplash)
        self.connect(self.topicCombobox, SIGNAL("currentIndexChanged(QString)"),self.updateTextEdit)

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
        self.hide()
    def updateTextEdit(self,currentTopic):
        self.textEdit.clear()
        if len(self.topicList)>0:
            self.setupTopicWindow(currentTopic)
    def setupTopicWindow(self,topic):
        for i,t in enumerate(self.topicList):
            if t==topic:
                self.topicCombobox.setCurrentIndex(i)
                break
        try:
            file=open(topic,'r')
            file.close()
            topicText=self.getTopicFileText(topic)
            self.textEdit.setPlainText(topicText)
        except:
            file=open(topic,'w')
            file.close()
    def deleteCurrentTopic(self):
        topic=self.topicCombobox.currentText()
        topicIndex=self.topicCombobox.currentIndex()
        self.deleteTopic(topic,topicIndex)
    def deleteTopic(self,topic,index=0):
        for i,t in enumerate(self.topicList):
            if t==topic and i==index:
                self.topicList.remove(topic)
                break
        file=open("arrayList",'r')
        self.topicCombobox.removeItem(index)
        self.delFromSplash(topic)
        os.remove(str(topic))

        if(len(self.topicList)>0):
            topic=self.topicList[0]
            self.setupTopicWindow(topic)
            self.delButton.setEnabled(True)
        else:
            self.saveButton.setEnabled(False)
            self.topicCombobox.setEnabled(False)
            self.delButton.setEnabled(False)
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
