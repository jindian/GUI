Required: python 2.7, PyQt4

After PyQt4 installed, design graphic user interface with Qt Desinger.

Save the GUI configuration, which is an XML with .ui postfixed file.

Below is an example of loading GUI configuraiton:

```python

import sys
from PyQt4 import QtCore, QtGui, uic

# UI file
qtUiFile = "example.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtUiFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())

```

Add routines to response behaviors from user.


--END--
