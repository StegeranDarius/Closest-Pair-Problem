from PyQt5 import QtCore, QtGui, QtWidgets
import mainview

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    plotter = mainview.Plotter()
    plotter.show()
    app.exec_()