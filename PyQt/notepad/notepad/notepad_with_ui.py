#!/usr/bin/python

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
        
        newWin = Notepad()
        newWin.show()

    def openResp(self):
        print sys._getframe().f_code.co_name

        self.file = QtGui.QFileDialog.getOpenFileName(self, 'Open File', ".", "(*.*)")
        if self.file:
            with open(self.file, "rt") as file:
                self.textEdit.setText(file.read())

    def saveResp(self):
        print sys._getframe().f_code.co_name

        if not self.file:
            self.file = QtGui.QFileDialog.getSaveFileName(self, 'Save File')

        with open(self.file, "wt") as file:
            file.write(self.textEdit.toPlainText())

    def printResp(self):
        print sys._getframe().f_code.co_name
        
        dialog = QtGui.QPrintDialog()
        dialog.setWindowTitle(self.file)

        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.textEdit.document().print_(dialog.printer())

    def previewResp(self):
        print sys._getframe().f_code.co_name

        preview = QtGui.QPrintPreviewDialog()
        preview.setWindowTitle(self.file)

        preview.paintRequested.connect(lambda p: self.textEdit.print_(p))
        
        preview.exec_()

    def cutResp(self):
        print sys._getframe().f_code.co_name

        self.textEdit.cut()

    def copyResp(self):
        print sys._getframe().f_code.co_name

        self.textEdit.copy()

    def pasteResp(self):
        print sys._getframe().f_code.co_name

        self.textEdit.paste()

    def undoResp(self):
        print sys._getframe().f_code.co_name

        self.textEdit.undo()

    def redoResp(self):
        print sys._getframe().f_code.co_name

        self.textEdit.redo()

    def bulletResp(self):
        print sys._getframe().f_code.co_name

        cursor = self.textEdit.textCursor()

        cursor.insertList(QtGui.QTextListFormat.ListDisc)

    def numberResp(self):
        print sys._getframe().f_code.co_name

        cursor = self.textEdit.textCursor()

        cursor.insertList(QtGui.QTextListFormat.ListDecimal)

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