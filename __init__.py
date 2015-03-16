__author__ = 'pyordan'

from splash import *
#buttonArray=[]

class mainDialog(splashDialog):

    def __init__(self,parent=None):
        super(mainDialog,self).__init__(parent)
        self.setupUI()
        #self.connect(self.addbut,SIGNAL("clicked()"),self.addButtonClicked)
        #if self.addButtonIsClicked:
            #print "add button is clicked"
            #self.atui= addTopicUi()
        #self.hide()
        #self.atui.setupUi()
                #self.atui=addTopicUi()




app=QApplication(sys.argv)
form=mainDialog()
form.show()
app.exec_()
