# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class SelfCarryAddress(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(633, 540)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setObjectName("textBrowser")

        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # 调整之后
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout.addWidget(self.textBrowser)

        self.horizontalLayout_2.addStretch(1)
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.horizontalLayout_2.addStretch(1)

        self.horizontalLayout_3.addStretch(1)
        self.horizontalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.horizontalLayout_3.addStretch(1)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.setOne)

        self.horizontalLayout_4.addStretch(1)
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.horizontalLayout_4.addStretch(1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">设置自搬移范围和自搬移地址，十六进制形式，格式如下。<br/>自搬移范围：0x111 ~ 0x222<br>自搬移地址：0x333</p></body></html>"))
        self.label.setText(_translate("Form", "自搬移范围："))
        self.label_2.setText(_translate("Form", "自搬移地址："))
        self.lineEdit.setText(_translate("Form", "0x1000"))
        self.lineEdit_2.setText(_translate("Form", "0x33f00000"))
        self.pushButton.setText(_translate("Form", "确定"))

        self.label_3.setText(_translate("Form", "~"))
        self.lineEdit_3.setText(_translate("Form", "0x3cefc"))

    def setOne(self):
        print('ffff')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = SelfCarryAddress()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())