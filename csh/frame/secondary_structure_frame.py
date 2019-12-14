# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 540)

        self.horizontalLayout = QtWidgets.QHBoxLayout()  # 创建H1
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.centrolWidget = QtWidgets.QWidget(MainWindow) # 创建中央widget
        self.centrolWidget.setObjectName("centrolWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centrolWidget)  # 创建V1(在Form的基础上建立V1)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()  # 创建H2
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        #
        self.stackedWidget = QtWidgets.QStackedWidget(self.centrolWidget)  # 创建stackWidget
        self.stackedWidget.setObjectName("stackedWidget")
        #
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.label = QtWidgets.QLabel(self.centrolWidget)
        self.label.setStyleSheet("font: 28pt \"黑体\";")
        self.label.setObjectName("label")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        #
        self.listWidget = QtWidgets.QListWidget(self.centrolWidget)
        self.listWidget.setObjectName("listWidget")

        #
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(28)
        item.setFont(font)
        self.listWidget.addItem(item)

        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(28)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable)
        self.listWidget.addItem(item)

        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(28)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable)
        self.listWidget.addItem(item)

        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(28)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable)
        self.listWidget.addItem(item)

        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(28)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable)
        self.listWidget.addItem(item)

        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(28)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable)
        self.listWidget.addItem(item)

        self.horizontalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout_2.setStretch(0,2)
        self.horizontalLayout_2.setStretch(1,5)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centrolWidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate('MainWIndow', '加载linux内核'))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "步骤一"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "步骤二"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "步骤三"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "步骤四"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "步骤五"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "步骤六"))
        self.listWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
