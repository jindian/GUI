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

        # Add widget to tool bar is not supported in QtDesigner,
        # and in QtDesigner, it's impossible to distinguish specific separator,
        # add widget with insertWidget interface,
        # add separator after font size with insertSeparator interface.

        # Font type
        self.fontBox = QtGui.QFontComboBox(self)
        self.Format.insertWidget(self.actionFontColor, self.fontBox)
        
        # Font size
        self.fontSize = QtGui.QComboBox(self)
        self.fontSize.setEditable(True)
        self.fontSize.setMinimumContentsLength(3)
        for i in range(6, 30):
            self.fontSize.addItem(str(i))
        self.Format.insertWidget(self.actionFontColor, self.fontSize)

        self.Format.insertSeparator(self.actionFontColor)
        

    def mapOperations(self):
        # Actions added by QtDesigner,
        # Response routine of every actions already done with QtDesigner.

        # Response mapping couldn't configure with QtDesigner added from here.
        # Widgets added by code.
        self.fontBox.currentFontChanged.connect(self.fontResp)
        self.fontSize.activated.connect(self.fontSizeResp)

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

    def fontResp(self, font):
        print sys._getframe().f_code.co_name

        self.textEdit.setCurrentFont(font)

    def fontSizeResp(self, fontsize):
        print sys._getframe().f_code.co_name
        # TODO:
        # Bug: font size not changed for some selected fontsize

        self.textEdit.setFontPointSize(fontsize)

    def fontColorResp(self):
        print sys._getframe().f_code.co_name

        color = QtGui.QColorDialog.getColor()
        self.textEdit.setTextColor(color)

    def backColorResp(self):
        print sys._getframe().f_code.co_name

        color = QtGui.QColorDialog.getColor()
        self.textEdit.setTextBackgroundColor(color)

    def boldResp(self):
        print sys._getframe().f_code.co_name

        format = self.textEdit.textCursor().charFormat()
        weight = format.fontWeight()
        if weight == QtGui.QFont.Bold:
            format.setFontWeight(QtGui.QFont.Normal)
        else:
            format.setFontWeight(QtGui.QFont.Bold)
        self.textEdit.textCursor().mergeCharFormat(format)

    def italicResp(self):
        print sys._getframe().f_code.co_name
        
        format = self.textEdit.textCursor().charFormat()
        italic = format.fontItalic()
        format.setFontItalic(not italic)
        self.textEdit.textCursor().mergeCharFormat(format)


    def underlResp(self):
        print sys._getframe().f_code.co_name

        format = self.textEdit.textCursor().charFormat()
        underl = format.fontUnderline()
        format.setFontUnderline(not underl)
        self.textEdit.textCursor().mergeCharFormat(format)

    def strikeResp(self):
        print sys._getframe().f_code.co_name

        format = self.textEdit.textCursor().charFormat()
        strike = format.fontStrikeOut()
        format.setFontStrikeOut(not strike)
        self.textEdit.textCursor().mergeCharFormat(format)

    def superResp(self):
        print sys._getframe().f_code.co_name

        format = self.textEdit.textCursor().charFormat()
        super = format.verticalAlignment()
        if super == QtGui.QTextCharFormat.AlignSuperScript:
            format.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)
        else:
            format.setVerticalAlignment(QtGui.QTextCharFormat.AlignSuperScript)
        self.textEdit.textCursor().mergeCharFormat(format)
            

    def subResp(self):
        print sys._getframe().f_code.co_name

        format = self.textEdit.textCursor().charFormat()
        super = format.verticalAlignment()
        if super == QtGui.QTextCharFormat.AlignSubScript:
            format.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)
        else:
            format.setVerticalAlignment(QtGui.QTextCharFormat.AlignSubScript)
        self.textEdit.textCursor().mergeCharFormat(format)

    def alignLeftResp(self):
        print sys._getframe().f_code.co_name

    def alignCenterResp(self):
        print sys._getframe().f_code.co_name

    def alignRightResp(self):
        print sys._getframe().f_code.co_name

    def alignJustifyResp(self):
        print sys._getframe().f_code.co_name

    def indentResp(relf):
        print sys._getframe().f_code.co_name

    def dedentResp(self):
        print sys._getframe().f_code.co_name

    def toggleToolbarResp(self):
        print sys._getframe().f_code.co_name

    def toggleFormatbarResp(self):
        print sys._getframe().f_code.co_name

    def toggleStatusbarResp(self):
        print sys._getframe().f_code.co_name

def main():
    app = QtGui.QApplication(sys.argv)

    window = Notepad()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()