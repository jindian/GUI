import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

class Notepad(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setupUI()

    def initToolbar(self):
        self.toolbar = self.addToolBar("Options")
        # Make next tool bar appear underneath this toolbar
        self.addToolBarBreak()

    def initFormatbar(self):
        self.formatbar = self.addToolBar("Format")

    def initMenubar(self):
        self.menubar = self.menuBar()

        self.file = self.menubar.addMenu("File")
        self.edit = self.menubar.addMenu("Edit")
        self.view = self.menubar.addMenu("View")
       

    def setupUI(self):
        # Initialize text area
        self.text = QtGui.QTextEdit(self)
        # Set QTextEdit object as central widget of the main window
        # This makes the QTextEdit object take up the window's entire space
        self.setCentralWidget(self.text)

        # Create tool bars
        # The two tool bars appear at the top of our window
        # The tool bars contain file management(opening a file, saving a file etc) or text-formatting
        self.initToolbar()
        self.initFormatbar()

        # Create a set of drop-down menus at the top of the screen
        self.initMenubar()

        # Create status bar at the button of the window
        self.statusbar = self.statusBar()

        # Set geometry of notepad with x, y, width, height
        self.setGeometry(100, 100, 1030, 800)

        self.setWindowTitle("Notepad")

def main():
    app = QtGui.QApplication(sys.argv)
    main = Notepad()
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()