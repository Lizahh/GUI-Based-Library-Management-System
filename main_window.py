# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 662)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 901, 631))
        self.tabWidget.setObjectName("tabWidget")
        self.dashboard_tab = QtWidgets.QWidget()
        self.dashboard_tab.setObjectName("dashboard_tab")
        self.widget = QtWidgets.QWidget(self.dashboard_tab)
        self.widget.setGeometry(QtCore.QRect(9, 9, 77, 85))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.new_book_btn = QtWidgets.QPushButton(self.widget)
        self.new_book_btn.setObjectName("new_book_btn")
        self.verticalLayout_5.addWidget(self.new_book_btn)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.widget1 = QtWidgets.QWidget(self.dashboard_tab)
        self.widget1.setGeometry(QtCore.QRect(9, 100, 881, 501))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.issued_books_table = QtWidgets.QTableWidget(self.widget1)
        self.issued_books_table.setColumnCount(8)
        self.issued_books_table.setObjectName("issued_books_table")
        self.issued_books_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.issued_books_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.issued_books_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.issued_books_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.issued_books_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.issued_books_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.issued_books_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.issued_books_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.issued_books_table.setHorizontalHeaderItem(7, item)
        self.horizontalLayout.addWidget(self.issued_books_table)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.delete_issued = QtWidgets.QPushButton(self.widget1)
        self.delete_issued.setObjectName("delete_issued")
        self.verticalLayout.addWidget(self.delete_issued)
        self.edit_issued = QtWidgets.QPushButton(self.widget1)
        self.edit_issued.setObjectName("edit_issued")
        self.verticalLayout.addWidget(self.edit_issued)
        self.refresh_issued = QtWidgets.QPushButton(self.widget1)
        self.refresh_issued.setObjectName("refresh_issued")
        self.verticalLayout.addWidget(self.refresh_issued)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.unissued_books_table = QtWidgets.QTableWidget(self.widget1)
        self.unissued_books_table.setColumnCount(8)
        self.unissued_books_table.setObjectName("unissued_books_table")
        self.unissued_books_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.unissued_books_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.unissued_books_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.unissued_books_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.unissued_books_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.unissued_books_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.unissued_books_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.unissued_books_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.unissued_books_table.setHorizontalHeaderItem(7, item)
        self.horizontalLayout_2.addWidget(self.unissued_books_table)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.delete_unissued = QtWidgets.QPushButton(self.widget1)
        self.delete_unissued.setObjectName("delete_unissued")
        self.verticalLayout_2.addWidget(self.delete_unissued)
        self.edit_unissued = QtWidgets.QPushButton(self.widget1)
        self.edit_unissued.setObjectName("edit_unissued")
        self.verticalLayout_2.addWidget(self.edit_unissued)
        self.refresh_unissued = QtWidgets.QPushButton(self.widget1)
        self.refresh_unissued.setObjectName("refresh_unissued")
        self.verticalLayout_2.addWidget(self.refresh_unissued)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.tabWidget.addTab(self.dashboard_tab, "")
        self.find_tab = QtWidgets.QWidget()
        self.find_tab.setObjectName("find_tab")
        self.widget2 = QtWidgets.QWidget(self.find_tab)
        self.widget2.setGeometry(QtCore.QRect(10, 0, 881, 601))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.search_input = QtWidgets.QLineEdit(self.widget2)
        self.search_input.setObjectName("search_input")
        self.horizontalLayout_4.addWidget(self.search_input)
        self.search_btn = QtWidgets.QPushButton(self.widget2)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_4.addWidget(self.search_btn)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.search_table = QtWidgets.QTableWidget(self.widget2)
        self.search_table.setColumnCount(8)
        self.search_table.setObjectName("search_table")
        self.search_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.search_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.search_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.search_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.search_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.search_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.search_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.search_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.search_table.setHorizontalHeaderItem(7, item)
        self.verticalLayout_8.addWidget(self.search_table)
        self.tabWidget.addTab(self.find_tab, "")
        self.all_books_tab = QtWidgets.QWidget()
        self.all_books_tab.setObjectName("all_books_tab")
        self.all_books_table = QtWidgets.QTableWidget(self.all_books_tab)
        self.all_books_table.setGeometry(QtCore.QRect(30, 70, 861, 521))
        self.all_books_table.setColumnCount(8)
        self.all_books_table.setObjectName("all_books_table")
        self.all_books_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.all_books_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_books_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_books_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_books_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_books_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_books_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_books_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_books_table.setHorizontalHeaderItem(7, item)
        self.widget3 = QtWidgets.QWidget(self.all_books_tab)
        self.widget3.setGeometry(QtCore.QRect(30, 0, 91, 59))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.refresh_btn = QtWidgets.QPushButton(self.widget3)
        self.refresh_btn.setObjectName("refresh_btn")
        self.verticalLayout_9.addWidget(self.refresh_btn)
        self.tabWidget.addTab(self.all_books_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Actions"))
        self.new_book_btn.setText(_translate("MainWindow", "New Book"))
        self.label_2.setText(_translate("MainWindow", "Books"))
        self.label_3.setText(_translate("MainWindow", "Issued Books"))
        item = self.issued_books_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.issued_books_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.issued_books_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        item = self.issued_books_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Isbn"))
        item = self.issued_books_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Page_Count"))
        item = self.issued_books_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Issued"))
        item = self.issued_books_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Author"))
        item = self.issued_books_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Year"))
        self.delete_issued.setText(_translate("MainWindow", "Delete"))
        self.edit_issued.setText(_translate("MainWindow", "Edit"))
        self.refresh_issued.setText(_translate("MainWindow", "Refresh"))
        self.label_4.setText(_translate("MainWindow", "Unissued Books"))
        item = self.unissued_books_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.unissued_books_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.unissued_books_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        item = self.unissued_books_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Isbn"))
        item = self.unissued_books_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Page_Count"))
        item = self.unissued_books_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Issued"))
        item = self.unissued_books_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Author"))
        item = self.unissued_books_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Year"))
        self.delete_unissued.setText(_translate("MainWindow", "Delete"))
        self.edit_unissued.setText(_translate("MainWindow", "Edit"))
        self.refresh_unissued.setText(_translate("MainWindow", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dashboard_tab), _translate("MainWindow", "Dashboard"))
        self.label_5.setText(_translate("MainWindow", "Search By Id"))
        self.search_btn.setText(_translate("MainWindow", "Search"))
        item = self.search_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.search_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.search_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        item = self.search_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Isbn"))
        item = self.search_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Page_Count"))
        item = self.search_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Issued"))
        item = self.search_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Author"))
        item = self.search_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Year"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.find_tab), _translate("MainWindow", "Find"))
        item = self.all_books_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.all_books_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.all_books_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        item = self.all_books_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Isbn"))
        item = self.all_books_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Page_Count"))
        item = self.all_books_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Issued"))
        item = self.all_books_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Author"))
        item = self.all_books_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Year"))
        self.label_6.setText(_translate("MainWindow", "All books"))
        self.refresh_btn.setText(_translate("MainWindow", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.all_books_tab), _translate("MainWindow", "All Books"))