
import sys
from PyQt4 import QtCore, QtGui, uic

# UI file
qtUiFile = "TaxCalculator.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtUiFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.TaxCalculateButton.clicked.connect(self.TaxCalculate)

	def TaxCalculate(self):
		price = int(self.PriceTextEdit.toPlainText())
		tax = (self.TaxRateSpinBox.value())
		total_price = price*(100+tax)/100
		self.TotalPriceTextEdit.setText(str(total_price))
		return


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())
