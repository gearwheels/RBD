import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QAction, QDialog

from logWin import Ui_LoginWindow
from MainWin import Ui_TransportCompanyWindow

class generalMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sizeWindow = QRect(QApplication.desktop().screenGeometry())
        self.width = int(self.sizeWindow.width())
        self.height = int(self.sizeWindow.height())


class mainMenuWindow(generalMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TransportCompanyWindow()
        self.ui.setupUi(self)
        self.loginDialogWindow = loginDialogWindow() # стартовое диалоговое окно для регистрации в программе 
        self.loginDialogWindow.exec_() # его запуск в отдельном потоке
        self.resize(self.width/2, self.height/2)

class generalDialogWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.sizeWindow = QRect(QApplication.desktop().screenGeometry())
        self.width = int(self.sizeWindow.width())
        self.height = int(self.sizeWindow.height())
        

class loginDialogWindow(generalDialogWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.resize(self.width/2, self.height/2)
        self.ui.btnEnter.clicked.connect(self.openTransportWin)

    def openTransportWin(self):
        if self.ui.comboBox.currentText() == "Транспортная компания":
            self.close()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    # loginDialogWin = loginDialogWindow()
    # loginDialogWin.show()
    MainWindow = mainMenuWindow()
    MainWindow.show()


    # print("TEST")

    sys.exit(app.exec_())

 