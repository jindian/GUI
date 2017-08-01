
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

    def setupNotepadUi(self):
        # Set QTextEdit object as the central widget of the window.
        self.setCentralWidget(self.textEdit)

def main():
    app = QtGui.QApplication(sys.argv)

    window = Notepad()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()