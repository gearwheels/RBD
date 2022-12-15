from PyQt5 import QtCore, QtGui, QtWidgets
from db import *

class Ui_TransportCompanyWindow(object):
    def setupUi(self, TransportCompanyWindow):
        TransportCompanyWindow.setObjectName("TransportCompanyWindow")
        TransportCompanyWindow.resize(1340, 871)
        font = QtGui.QFont()
        font.setPointSize(14)
        TransportCompanyWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(TransportCompanyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(16)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioBtnDriver = QtWidgets.QRadioButton(self.centralwidget)
        self.radioBtnDriver.setObjectName("radioBtnDriver")
        self.verticalLayout_2.addWidget(self.radioBtnDriver)
        self.radioBtnTransportCompany = QtWidgets.QRadioButton(self.centralwidget)
        self.radioBtnTransportCompany.setObjectName("radioBtnTransportCompany")
        self.verticalLayout_2.addWidget(self.radioBtnTransportCompany)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnCheck = QtWidgets.QPushButton(self.centralwidget)
        self.btnCheck.setObjectName("btnCheck")
        self.btnCheck.clicked.connect(self.Show_tabel)
        self.verticalLayout.addWidget(self.btnCheck)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 8)
        self.horizontalLayout.setStretch(2, 4)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setObjectName("btnAdd")
        self.btnAdd.clicked.connect(self.Add_data_to_tabel)
        self.horizontalLayout_2.addWidget(self.btnAdd)
        self.horizontalLayout_2.setStretch(0, 10)
        self.horizontalLayout_2.setStretch(1, 3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        TransportCompanyWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TransportCompanyWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1340, 31))
        self.menubar.setObjectName("menubar")
        TransportCompanyWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TransportCompanyWindow)
        self.statusbar.setObjectName("statusbar")
        TransportCompanyWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TransportCompanyWindow)
        QtCore.QMetaObject.connectSlotsByName(TransportCompanyWindow)

    def retranslateUi(self, TransportCompanyWindow):
        _translate = QtCore.QCoreApplication.translate
        TransportCompanyWindow.setWindowTitle(_translate("TransportCompanyWindow", "Транспортная компания"))
        self.radioBtnDriver.setText(_translate("TransportCompanyWindow", "Водители"))
        self.radioBtnTransportCompany.setText(_translate("TransportCompanyWindow", "Транспортные фирмы"))
        self.btnCheck.setText(_translate("TransportCompanyWindow", "Смотреть"))
        self.btnAdd.setText(_translate("TransportCompanyWindow", "Добавить"))


    def Show_tabel(self):
        while(self.tableWidget.rowCount() > 0):
            self.tableWidget.removeRow(0)
        if self.radioBtnDriver.isChecked():
            name_table = 'driver'
        elif self.radioBtnTransportCompany.isChecked():
            name_table = 'management_company'
        else:
            return
        data = connect(func=Get_data_from_table, name_table=name_table)
        for tuple in data:
            self.tableWidget.insertRow(self.tableWidget.rowCount()) 
            self.tableWidget.setColumnCount(len(tuple))
            for i, t in enumerate(tuple):
                item = QtWidgets.QTableWidgetItem(str(t))
                self.tableWidget.setItem(self.tableWidget.rowCount()-1, i, item) 
        self.tableWidget.insertRow(self.tableWidget.rowCount()) 
        item = QtWidgets.QTableWidgetItem(str(self.tableWidget.rowCount()))
        self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, item) 
    
    def Add_data_to_tabel(self):
        if self.radioBtnDriver.isChecked():
            name_table = 'driver'
        elif self.radioBtnTransportCompany.isChecked():
            name_table = 'management_company'
        data = []
        try:
            i = self.tableWidget.rowCount() - 1
            for j in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(i, j)
                data += [item.text()]
        except:
            print("ошибка")
            data = []
        if len(data) != 0:
            for i, d in enumerate(data):
                print(i, d)
            connect(Insert_data_to_table, name_table, data) 
            self.tableWidget.insertRow(self.tableWidget.rowCount()) 
            item = QtWidgets.QTableWidgetItem(str(self.tableWidget.rowCount()))
            self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, item)     

       
