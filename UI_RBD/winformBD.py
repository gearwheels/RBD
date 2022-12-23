import sys
from db import *
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QAction, QDialog, QLineEdit

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
        self.ui.btnCheck.clicked.connect(self.Show_tabel)
        self.ui.btnAdd.clicked.connect(self.Add_data_to_tabel)

    def back(self):
        self.hide()

        self.loginDialogWindow.show() # его запуск в отдельном потоке

    def Show_tabel(self):
        while(self.ui.tableWidget.rowCount() > 0):
            self.ui.tableWidget.removeRow(0)
        if self.ui.radioBtnDriver.isChecked():
            name_table = 'driver'
        elif self.ui.radioBtnTransportCompany.isChecked():
            name_table = 'management_company'
        else:
            return
        data = connect(func=Get_data_from_table, name_table=name_table)
        for tuple in data:
            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount()) 
            self.ui.tableWidget.setColumnCount(len(tuple)-1)
            for i, t in enumerate(tuple):
                if i == 0:
                    continue
                item = QtWidgets.QTableWidgetItem(str(t))
                self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount()-1, i-1, item) 
        self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount()) 
        # item = QtWidgets.QTableWidgetItem(str(self.ui.tableWidget.rowCount()))
        # self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount()-1, 0, item) 
    
    def Add_data_to_tabel(self):
        if self.ui.radioBtnDriver.isChecked():
            name_table = 'driver'
        elif self.ui.radioBtnTransportCompany.isChecked():
            name_table = 'management_company'
        data = []
        try:
            i = self.ui.tableWidget.rowCount() - 1
            for j in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(i, j)
                data += [item.text()]
        except:
            print("ошибка")
            data = []
        if len(data) != 0:
            for i, d in enumerate(data):
                print(i, d)
            connect(Insert_data_to_table, name_table, data) 
            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount()) 
            item = QtWidgets.QTableWidgetItem(str(self.ui.tableWidget.rowCount()))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount()-1, 0, item)     


    

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
        self.ui.btnEnter.clicked.connect(self.checkLogin)
        self.myLogin = "admin"
        self.password = "1234"
        quit = QAction("Quit", self) # событие выхода
        quit.triggered.connect(self.closeEvent) # если событие выхода срабатывает то вызывается closeEvent
        self.ui.lineEdit_2.setEchoMode(QLineEdit.Password)


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

    def checkLogin(self):
        warning = QMessageBox()
        warning.setWindowTitle("Предупреждение")

        warning.setDefaultButton(QMessageBox.Ok)

        if self.ui.lineEdit.text() != self.myLogin:
            warning.setText("Неправильный логин.")
            warning = warning.exec()
        elif self.ui.lineEdit_2.text() != self.password:
            warning.setText("Неправильный пароль.")
            warning = warning.exec()
        else:
            self.openTransportWin()

    def closeEvent(self, event):
        if self.ui.btnEnter.isChecked(): # если closeEvent вызван и при этом нажата кнопка подписи отчета
            event.accept() # то не выводим диалоговое окно подтверждения выхода из проги
        else: # иначе формируем окно подтверждения выхода из проги (т.е QMessageBox)
            close = QMessageBox()
            close.setWindowTitle("Закрыть приложение")
            close.setText("Вы уверены, что хотите закрыть приложение?") #
            close.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) #
            close = close.exec()
            if close == QMessageBox.Ok: # если нажали да
                event.accept() # подтверждаем ивент
                sys.exit()
            else: # иначе игнорируем
                event.ignore()
        self.ui.btnEnter.setChecked(False)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    # loginDialogWin = loginDialogWindow()
    # loginDialogWin.show()
    MainWindow = mainMenuWindow()
    MainWindow.show()


    # print("TEST")

    sys.exit(app.exec_())

 