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
        e= self.height()
        self.setFixedWidth(self.width())
        self.setMaximumHeight(658)
        print e

        thread.start_new_thread(self.check_size,(e,))


    def check_size(self,x):
        while True:
            #time.sleep(2)
            #print self.height()
            self.textEdit.setFixedHeight(self.height())
            self.textEdit.setFixedWidth(self.width())