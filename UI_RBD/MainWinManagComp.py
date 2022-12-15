# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWinManagComp.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.radioBtnRoute = QtWidgets.QRadioButton(self.centralwidget)
        self.radioBtnRoute.setObjectName("radioBtnRoute")
        self.verticalLayout_2.addWidget(self.radioBtnRoute)
        self.radioButtonSensor = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonSensor.setObjectName("radioButtonSensor")
        self.verticalLayout_2.addWidget(self.radioButtonSensor)
        self.radioBtnCamera = QtWidgets.QRadioButton(self.centralwidget)
        self.radioBtnCamera.setObjectName("radioBtnCamera")
        self.verticalLayout_2.addWidget(self.radioBtnCamera)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnCheck = QtWidgets.QPushButton(self.centralwidget)
        self.btnCheck.setObjectName("btnCheck")
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
        TransportCompanyWindow.setWindowTitle(_translate("TransportCompanyWindow", "Управляющая компания"))
        self.radioBtnDriver.setText(_translate("TransportCompanyWindow", "Водители"))
        self.radioBtnTransportCompany.setText(_translate("TransportCompanyWindow", "Транспортные фирмы"))
        self.radioBtnRoute.setText(_translate("TransportCompanyWindow", "Маршруты"))
        self.radioButtonSensor.setText(_translate("TransportCompanyWindow", "Сенсоры"))
        self.radioBtnCamera.setText(_translate("TransportCompanyWindow", "Камеры"))
        self.btnCheck.setText(_translate("TransportCompanyWindow", "Смотреть"))
        self.btnAdd.setText(_translate("TransportCompanyWindow", "Добавить"))
