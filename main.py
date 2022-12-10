from PyQt5 import QtWidgets

from BSpline.Interface.mainWindow import *

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    window = QtWidgets.QMainWindow()
    ui = MainWindow(window)
    window.show()
    sys.exit(app.exec_())
