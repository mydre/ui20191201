# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPalette, QColor, QIcon
from PyQt5.QtWidgets import QTabWidget
from csh.qwidgets.self_carry_address_seek import SelfCarryAddressSeek
from csh.frame.fill_secondary_structure_frame import Integrated
import tkinter
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 522)
        palette = QtGui.QPalette()
        icon = QtGui.QPixmap('./image/sky2.jpg')
        palette.setBrush(Form.backgroundRole(), QtGui.QBrush(icon))  # 添加背景图片
        #palette.setColor(Form.backgroundRole(), QColor(192, 253, 123))
        Form.setPalette(palette)
        #Form.color = QtGui.QColor(0, 0, 255)

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = Integrated()
        #self.tabWidget.setTabShape(QTabWidget.Triangular)  # 设置tab的显示样式
        self.tabWidget.setTabShape(QTabWidget.Rounded)

        palette0 = QPalette()
        palette0.setColor(self.tabWidget.backgroundRole(), QColor(0,0,123))
        self.tabWidget.setPalette(palette0)

        screen = tkinter.Tk()
        x = screen.winfo_screenwidth()
        #print(x)
        sss = str(x/7.0-3.8) + 'px'
        #print(sss)
        layo = "QTabWidget::pane{border-width: 10px;border-color:#7FFFD4;border-style:dashed	;background:white}" + \
            "QTabBar::tab{width:" + sss +"; height:85px;font:20px;color:green;background:#87CEEB}" + \
            "QTabWidget::tab-bar{alignment:center}" + \
            "QTabBar::tab:selected {color: rgb(36,197,219);background:#FFD700;font-weight:bold}"
        self.tabWidget.setStyleSheet(layo)




        # self.tab = QtWidgets.qwidgets()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        #self.tab_2 = QtWidgets.qwidgets()
        self.selfCarryAddressWidget = SelfCarryAddressSeek()
        self.tab_2 = self.selfCarryAddressWidget
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")

        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")

        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget.addTab(self.tab_7, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "扫描"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "静态逆向"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "动态调试"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "模糊测试"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "污点分析"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "符号执行"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Form", "木马"))
        self.tabWidget.setIconSize(QSize(65, 65))

        self.tabWidget.setTabIcon(self.tabWidget.indexOf(self.tab),QIcon('./image/saomiao.png'))
        self.tabWidget.setTabIcon(self.tabWidget.indexOf(self.tab_2),QIcon('./image/nixiang.png'))
        self.tabWidget.setTabIcon(self.tabWidget.indexOf(self.tab_3),QIcon('./image/tiaoshi.png'))
        self.tabWidget.setTabIcon(self.tabWidget.indexOf(self.tab_4),QIcon('./image/ceshi.png'))
        self.tabWidget.setTabIcon(self.tabWidget.indexOf(self.tab_5),QIcon('./image/wudian.png'))
        self.tabWidget.setTabIcon(self.tabWidget.indexOf(self.tab_6),QIcon('./image/fuhao.png'))
        self.tabWidget.setTabIcon(self.tabWidget.indexOf(self.tab_7),QIcon('./image/muma.png'))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())