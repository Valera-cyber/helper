# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './View/Setting_helper/Setting_helper.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(467, 386)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_base = QtWidgets.QWidget()
        self.tab_base.setObjectName("tab_base")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_base)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.tab_base)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_path = QtWidgets.QLineEdit(self.tab_base)
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.horizontalLayout.addWidget(self.lineEdit_path)
        self.btn_path = QtWidgets.QPushButton(self.tab_base)
        self.btn_path.setObjectName("btn_path")
        self.horizontalLayout.addWidget(self.btn_path)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(self.tab_base)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_pathExport = QtWidgets.QLineEdit(self.tab_base)
        self.lineEdit_pathExport.setObjectName("lineEdit_pathExport")
        self.gridLayout_2.addWidget(self.lineEdit_pathExport, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_base)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.tabWidget.addTab(self.tab_base, "")
        self.tab_branch = QtWidgets.QWidget()
        self.tab_branch.setObjectName("tab_branch")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_branch)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_add_edit_branch = QtWidgets.QLineEdit(self.tab_branch)
        self.lineEdit_add_edit_branch.setText("")
        self.lineEdit_add_edit_branch.setClearButtonEnabled(True)
        self.lineEdit_add_edit_branch.setObjectName("lineEdit_add_edit_branch")
        self.horizontalLayout_6.addWidget(self.lineEdit_add_edit_branch)
        self.btn_add_edit_branch = QtWidgets.QPushButton(self.tab_branch)
        self.btn_add_edit_branch.setObjectName("btn_add_edit_branch")
        self.horizontalLayout_6.addWidget(self.btn_add_edit_branch)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.table_branch = QtWidgets.QTableWidget(self.tab_branch)
        self.table_branch.setObjectName("table_branch")
        self.table_branch.setColumnCount(0)
        self.table_branch.setRowCount(0)
        self.verticalLayout_4.addWidget(self.table_branch)
        self.tabWidget.addTab(self.tab_branch, "")
        self.tab_department = QtWidgets.QWidget()
        self.tab_department.setObjectName("tab_department")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_department)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_department = QtWidgets.QLineEdit(self.tab_department)
        self.lineEdit_department.setClearButtonEnabled(True)
        self.lineEdit_department.setObjectName("lineEdit_department")
        self.horizontalLayout_2.addWidget(self.lineEdit_department)
        self.btn_add_edit = QtWidgets.QPushButton(self.tab_department)
        self.btn_add_edit.setObjectName("btn_add_edit")
        self.horizontalLayout_2.addWidget(self.btn_add_edit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.table_department = QtWidgets.QTableWidget(self.tab_department)
        self.table_department.setObjectName("table_department")
        self.table_department.setColumnCount(0)
        self.table_department.setRowCount(0)
        self.verticalLayout_3.addWidget(self.table_department)
        self.tabWidget.addTab(self.tab_department, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_save = QtWidgets.QPushButton(Dialog)
        self.btn_save.setObjectName("btn_save")
        self.gridLayout.addWidget(self.btn_save, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.btn_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout.addWidget(self.btn_cancel, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Путь к базе данных:"))
        self.btn_path.setText(_translate("Dialog", "Открыть"))
        self.label_2.setText(_translate("Dialog", "Путь к рабочему каталогу:"))
        self.pushButton_2.setText(_translate("Dialog", "Открыть"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_base), _translate("Dialog", "База данных"))
        self.lineEdit_add_edit_branch.setPlaceholderText(_translate("Dialog", "Новый филиал"))
        self.btn_add_edit_branch.setText(_translate("Dialog", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_branch), _translate("Dialog", "Филиал"))
        self.lineEdit_department.setPlaceholderText(_translate("Dialog", "Новая служба"))
        self.btn_add_edit.setText(_translate("Dialog", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_department), _translate("Dialog", "Службы"))
        self.btn_save.setText(_translate("Dialog", "Сохранить"))
        self.btn_cancel.setText(_translate("Dialog", "Отмена"))
