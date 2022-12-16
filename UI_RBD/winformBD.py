import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QAction, QDialog

from logWin import Ui_LoginWindow
from MainWinTransComp import Ui_TransportCompanyWindow
from MainWinRoadComp import Ui_RoadCompanyWindow
from MainWinManagComp import Ui_ManagementCompanyWindow

class generalMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sizeWindow = QRect(QApplication.desktop().screenGeometry())
        self.width = int(self.sizeWindow.width())
        self.height = int(self.sizeWindow.height())


class mainMenuWindow(generalMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ManagementCompanyWindow()
        self.ui.setupUi(self)
        self.loginDialogWindow = loginDialogWindow(self) # стартовое диалоговое окно для регистрации в программе 
        self.loginDialogWindow.exec_() # его запуск в отдельном потоке
        self.resize(self.width/2, self.height/2)

        self._connectionInit()

    def _connectionInit(self):
        self.ui.btnBack.clicked.connect(self.back)

    def back(self):
        self.hide()

        self.loginDialogWindow.show() # его запуск в отдельном потоке
        

class generalDialogWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.sizeWindow = QRect(QApplication.desktop().screenGeometry())
        self.width = int(self.sizeWindow.width())
        self.height = int(self.sizeWindow.height())
        

class loginDialogWindow(generalDialogWindow):
    def __init__(self, root):
        super().__init__() # инициализация
        self.mainMenuWindow = root
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.resize(self.width/2, self.height/2)
        self.ui.btnEnter.clicked.connect(self.openTransportWin)

    def openTransportWin(self): # Ui_RoadCompanyWindow() Ui_ManagementCompanyWindow
        if self.ui.comboBox.currentText() == "Транспортная компания":
            self.mainMenuWindow.ui = Ui_TransportCompanyWindow()
        elif self.ui.comboBox.currentText() == "Дорожная компания":
            self.mainMenuWindow.ui = Ui_RoadCompanyWindow()
        elif self.ui.comboBox.currentText() == "Управляющая компания":
            self.mainMenuWindow.ui = Ui_ManagementCompanyWindow()
        
        self.mainMenuWindow.ui.setupUi(self.mainMenuWindow)
        self.mainMenuWindow._connectionInit()
        self.hide()
        self.mainMenuWindow.show()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    # loginDialogWin = loginDialogWindow()
    # loginDialogWin.show()
    MainWindow = mainMenuWindow()
    MainWindow.show()


    # print("TEST")

    sys.exit(app.exec_())

 