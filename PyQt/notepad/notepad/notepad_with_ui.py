
import sys
from PyQt4 import QtGui, QtCore, uic
# from PyQt4.QtCore import Qt

# Qt Designer .ui file
notepadUI = "notepad.ui"

# Load a Qt Designer .ui file and 
# return a tuple of the generated form class and the Qt base class.
Ui_MainWindow, QtBaseClass = uic.loadUiType(notepadUI)

class Notepad(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Initialize main window
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        # Setup UI with resource from Qt Designer.
        self.setupUi(self)

        # Make some local modifications.
        self.setupNotepadUi()

        # Edit file
        self.file = ""

        # Map operations and response routines
        self.mapOperations()


    def setupNotepadUi(self):
        # Set QTextEdit object as the central widget of the window.
        self.setCentralWidget(self.textEdit)

    def mapOperations(self):
        self.actionNew.triggered.connect(self.newResp)
        self.actionOpen.triggered.connect(self.openResp)
        self.actionSave.triggered.connect(self.saveResp)
        self.actionPrint.triggered.connect(self.printResp)
        self.actionPreview.triggered.connect(self.previewResp)
        self.actionCut.triggered.connect(self.cutResp)
        self.actionCopy.triggered.connect(self.copyResp)
        self.actionPaste.triggered.connect(self.pasteResp)
        self.actionUndo.triggered.connect(self.undoResp)
        self.actionRedo.triggered.connect(self.redoResp)
        self.actionInsertBuuletList.triggered.connect(self.bulletResp)
        self.actionInsertNumberedList.triggered.connect(self.numberResp)
        self.textEdit.cursorPositionChanged.connect(self.cursorPositionResp)

    # Operation reponse routines start from here
    def newResp(self):
        print sys._getframe().f_code.co_name

    def openResp(self):
        print sys._getframe().f_code.co_name

    def saveResp(self):
        print sys._getframe().f_code.co_name

    def printResp(self):
        print sys._getframe().f_code.co_name

    def previewResp(self):
        print sys._getframe().f_code.co_name

    def cutResp(self):
        print sys._getframe().f_code.co_name

    def copyResp(self):
        print sys._getframe().f_code.co_name

    def pasteResp(self):
        print sys._getframe().f_code.co_name

    def undoResp(self):
        print sys._getframe().f_code.co_name

    def redoResp(self):
        print sys._getframe().f_code.co_name

    def bulletResp(self):
        print sys._getframe().f_code.co_name

    def numberResp(self):
        print sys._getframe().f_code.co_name

    def cursorPositionResp(self):
        print sys._getframe().f_code.co_name

        cursor = self.textEdit.textCursor()
        
        # Mortals like 1-indexed things
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()

        self.statusbar.showMessage("Line: {} | Column: {}".format(line,col))



def main():
    app = QtGui.QApplication(sys.argv)

    window = Notepad()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()