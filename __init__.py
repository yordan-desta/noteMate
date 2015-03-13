__author__ = 'pyordan'

from splash import *
buttonArray=[]

class mainDialog(splashDialog):

    def __init__(self,parent=None):
        super(mainDialog,self).__init__(parent)
        self.setupUI()


app=QApplication(sys.argv)
form=mainDialog()
form.show()
app.exec_()
