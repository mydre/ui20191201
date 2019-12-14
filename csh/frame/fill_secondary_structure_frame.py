# -*- coding: utf-8 -*-

"""
Module implementing QQShow.
"""

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from csh.frame.secondary_structure_frame import Ui_MainWindow
from csh.qwidgets.self_carry_address_seek import SelfCarryAddressSeek
from csh.qwidgets.free_field_address_seek import FreeFieldAddressSeek
from csh.qwidgets.jtk_point_seek import JtkPointSeek
from csh.qwidgets.relocation_point_seek import RelocationPointSeek
from csh.qwidgets.patch_seek import PatchSeek
from csh.qwidgets.multiple_parameters_seek import MultipleParametersSeek
import sys
import subprocess
import heapq
import re

class Integrated(QMainWindow, Ui_MainWindow):  # 传入的是UI_MainWindow，相当于是继承了Ui_MainWindow
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type qwidgets
        """
        super(Integrated, self).__init__(parent)
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.selfCarryAddressWidget = SelfCarryAddressSeek()
        self.freeFieldAddressWidget = FreeFieldAddressSeek()
        self.jtkPointSeekWidget = JtkPointSeek()
        self.relocationPointWidget = RelocationPointSeek()
        #self.patchWidget = SelectUntitled5()
        self.multipleParametersWidget = MultipleParametersSeek()
        self.patchWidget = PatchSeek()
        self.stackedWidget.addWidget(self.selfCarryAddressWidget)  # 使用从UI_MainWindow继承过来的stackedWidget

        self.stackedWidget.addWidget(self.jtkPointSeekWidget)
        self.stackedWidget.addWidget(self.relocationPointWidget)
        #self.stackedWidget.addWidget(self.patchWidget)
        self.stackedWidget.addWidget(self.multipleParametersWidget)
        self.stackedWidget.addWidget(self.freeFieldAddressWidget)
        self.stackedWidget.addWidget(self.patchWidget)

        self.selfCarryAddressWidget.pushButton.clicked.connect(self.setOne)
        self.freeFieldAddressWidget.pushButton.clicked.connect(self.setTwo_getEmptyAddress)
        self.freeFieldAddressWidget.pushButton_2.clicked.connect(self.setTwo_setEmptyAddress)
        self.jtkPointSeekWidget.pushButton.clicked.connect(self.setThree_JTKpoint)
        self.relocationPointWidget.pushButton.clicked.connect(self.setFour)
        self.multipleParametersWidget.pushButton.clicked.connect(self.setFive)
        self.multipleParametersWidget.pushButton_2.clicked.connect(self.doFive)
        self.patchWidget.pushButton.clicked.connect(self.doSix)
        # self.jtkPointSeekWidget.
        # 步骤一
        self.self_move_fanwei_1 = ''
        self.self_move_fanwei_2 = ''
        self.self_move_addr = ''
        self.freeSpaceAddress_begin = ''
        self.freeSpaceAddress_end = ''
        self.stepOneResult = ''  # 用于保存步骤一计算的结果，这个结果最后可以patch到backdoor.py对应的位置
        # 步骤二
        self.free_slots = 0
        # 步骤四
        self.rellocate_point = ''
        self.kenel_decompressed_address = ''
        # 步骤五
        self.kernel_start_address = ''
        self.hook_function = ''
        self.sys_call_table = ''
        self.sys_oabi_call_table = ''
        self.sys_execve_wrapper = ''
        self.syscall_execve_wrapper = ''

    def alter(self,file, pattern, new_str):
        file_data = ''
        with open(file, "r", encoding="utf-8") as f1:
            for line in f1:
                line = re.sub(pattern, new_str, line)
                file_data += line
        with open(file, "w", encoding="utf-8") as f:
            f.write(file_data)

    def alter_one(self,strs):
        self.alter('./csh/files/backdoor.py', 'patch_codes.append\(\(0xed8.*', 'patch_codes.append((0xed8, ' + strs + '))')

    def alter_three(self,strs):
        self.alter('./csh/files/backdoor.py',"patch_codes.append\(\(.*'BL 0xed4'.*", 'patch_codes.append((' + strs + ', ' + "'BL 0xed4'" + '))')

    def finder(self,file):
        with open(file, "r", encoding="utf-8") as f1:
            for line in f1:
                if 'sys_call_table' in line:
                    self.sys_call_table = '0x' + line.split(' ')[0]
                    # print('0x' + line.split(' ')[0])
                elif 'sys_oabi_call_table' in line:
                    self.sys_oabi_call_table = '0x' + line.split(' ')[0]
                elif 'sys_execve_wrapper' in line:
                    self.sys_execve_wrapper = '0x' + line.split(' ')[0]
                elif 'syscall_execve_wrapper' in line:
                    self.syscall_execve_wrapper = '0x' + line.split(' ')[0]

    @pyqtSlot(int)
    def on_listWidget_currentRowChanged(self, p0):
        """
        选择造型
        """
        # print('变了没')
        self.stackedWidget.setCurrentIndex(p0)
        # print(p0)

    @pyqtSlot(int)
    def on_stackedWidget_currentChanged(self, p0):
        """
        页面切换时
        """
        pass

    def setOne(self):
        # QMessageBox.information(self, "提示", "自搬移范围和自搬移大小设置成功！")
        self.self_move_fanwei_1 = self.selfCarryAddressWidget.lineEdit.text()
        self.self_move_fanwei_2 = self.selfCarryAddressWidget.lineEdit_3.text()
        self.self_move_addr = self.selfCarryAddressWidget.lineEdit_2.text()
        self.selfCarryAddressWidget.textBrowser.append('----------------------------------')
        self.selfCarryAddressWidget.textBrowser.append('自搬移范围格式：' + self.self_move_fanwei_1 + ' ~ ' + self.self_move_fanwei_2)
        self.selfCarryAddressWidget.textBrowser.append('自搬移地址格式：' + self.self_move_addr)
        self.stepOneResult = str(hex(int(self.self_move_fanwei_2,16) - int(self.self_move_fanwei_1,16) + int(self.self_move_addr,16)))
        # print(self.stepOneResult)
        self.alter_one(self.stepOneResult)
        self.selfCarryAddressWidget.textBrowser.append('修改成功：' + self.stepOneResult)
        self.selfCarryAddressWidget.pushButton.setEnabled(False)
        item = self.listWidget.item(1)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

    def setTwo_getEmptyAddress(self):
        a = subprocess.getstatusoutput('python2 ./csh/files/find_slots_in_bin.py')
        self.freeFieldAddressWidget.textBrowser.append('--------------------------------------------')
        self.freeFieldAddressWidget.textBrowser.append(a[1])
        address_list = a[1].split('\n')
        len = address_list.__len__()
        #print(len)
        addr_list = []  # 需要接着这个列表做处理
        addr_span_list = []
        for li in address_list[0:len-1]:
            ll = li.split(' ')
            addr_list.append(int(ll[-3],16))
            addr_list.append(int(ll[-2],16))
            addr_span_list.append(int(ll[-1],16))

        max_num_index_list = list(map(addr_span_list.index, heapq.nlargest(len-1, addr_span_list)))
        remain = 0x19b0
        j = 0
        for i in max_num_index_list:
            j = j + 1
            remain = remain - addr_span_list[i]
            if remain <= 0:
                break
        self.free_slots = j
        if(j <= 1):
            a = sorted(max_num_index_list[0:1])
            k = a[0]
            self.freeFieldAddressWidget.lineEdit.setText(str(hex(addr_list[k*2 + 1] - addr_span_list[k] - remain)))
            self.freeFieldAddressWidget.lineEdit_2.setText(str(hex(addr_list[k*2 + 1])))
        elif(j <= 2):
            a = sorted(max_num_index_list[0:2])
            k = a[0]
            self.freeFieldAddressWidget.lineEdit.setText(str(hex(addr_list[k * 2 + 1] - addr_span_list[k])))
            self.freeFieldAddressWidget.lineEdit_2.setText(str(hex(addr_list[k * 2 + 1])))
            k = a[1]
            self.freeFieldAddressWidget.lineEdit_3.setText(str(hex(addr_list[k * 2 + 1] - addr_span_list[k] - remain)))
            self.freeFieldAddressWidget.lineEdit_4.setText(str(hex(addr_list[k * 2 + 1])))
        elif(j <= 3):
            a = sorted(max_num_index_list[0:3])
            k = a[0]
            self.freeFieldAddressWidget.lineEdit.setText(str(hex(addr_list[k * 2 + 1] - addr_span_list[k])))
            self.freeFieldAddressWidget.lineEdit_2.setText(str(hex(addr_list[k * 2 + 1])))
            k = a[1]
            self.freeFieldAddressWidget.lineEdit_3.setText(str(hex(addr_list[k * 2 + 1] - addr_span_list[k])))
            self.freeFieldAddressWidget.lineEdit_4.setText(str(hex(addr_list[k * 2 + 1])))
            k = a[2]
            self.freeFieldAddressWidget.lineEdit_5.setText(str(hex(addr_list[k * 2 + 1] - addr_span_list[k] - remain)))
            self.freeFieldAddressWidget.lineEdit_6.setText(str(hex(addr_list[k * 2 + 1])))
        elif(j <= 4):
            a = sorted(max_num_index_list[0:4])
            k = a[0]
            self.freeFieldAddressWidget.lineEdit.setText(str(hex(addr_list[k * 2 + 1] - addr_span_list[k])))
            self.freeFieldAddressWidget.lineEdit_2.setText(str(hex(addr_list[k * 2 + 1])))
            k = a[1]
            self.freeFieldAddressWidget.lineEdit_3.setText(str(hex(addr_list[k * 2 + 1] - addr_span_list[k])))
            self.freeFieldAddressWidget.lineEdit_4.setText(str(hex(addr_list[k * 2 + 1])))
            k = a[2]
            self.freeFieldAddressWidget.lineEdit_5.setText(str(hex(addr_list[k * 2 + 1] - addr_span_list[k])))
            self.freeFieldAddressWidget.lineEdit_6.setText(str(hex(addr_list[k * 2 + 1])))
            k = a[3]
            self.freeFieldAddressWidget.lineEdit_7.setText(str(hex(addr_list[k * 2 + 1] - addr_span_list[k] - remain)))
            self.freeFieldAddressWidget.lineEdit_8.setText(str(hex(addr_list[k * 2 + 1])))
        else:
            print('空闲块的块数需要大于4！')
        self.freeFieldAddressWidget.pushButton.setEnabled(False)

    def setTwo_setEmptyAddress(self):

        pass

    # 步骤三方法
    def setThree_JTKpoint(self):
        self.jtkPointSeekWidget.textBrowser.append('---------------------')
        self.jtkPointSeekWidget.textBrowser.append('JTK point:' + self.jtkPointSeekWidget.lineEdit.text())
        self.alter_three(self.jtkPointSeekWidget.lineEdit.text())
        self.jtkPointSeekWidget.textBrowser.append('JTK point设置成功：' + self.jtkPointSeekWidget.lineEdit.text())
        self.jtkPointSeekWidget.pushButton.setEnabled(False)
        item = self.listWidget.item(2)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

    # 步骤四方法
    def setFour(self):
        self.relocationPointWidget.textBrowser.append('--------------------------')
        self.rellocate_point = self.relocationPointWidget.lineEdit.text()
        self.kenel_decompressed_address = self.relocationPointWidget.lineEdit_2.text()
        self.relocationPointWidget.textBrowser.append('rellocation point：' + self.rellocate_point)
        self.relocationPointWidget.textBrowser.append('内核解压头地址：' + self.kenel_decompressed_address)
        self.relocationPointWidget.pushButton.setEnabled(False)
        item = self.listWidget.item(3)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

    # 步骤五方法
    def setFive(self):
        self.finder('./csh/files/kallsyms.txt')
        self.multipleParametersWidget.lineEdit_2.setText(self.sys_call_table)
        self.multipleParametersWidget.lineEdit_3.setText(self.sys_oabi_call_table)
        self.multipleParametersWidget.lineEdit_4.setText(self.sys_execve_wrapper)
        if(self.syscall_execve_wrapper != ''):
            self.multipleParametersWidget.lineEdit_5.setText(self.syscall_execve_wrapper)
        self.multipleParametersWidget.pushButton.setEnabled(False)

    def alter_by_line(self,file,li,front,rear):
        file_data = ''
        with open(file, "r", encoding="utf-8") as f1:
            i = 0
            for line in f1:
                i = i+1
                if i == li:
                    line = '    .word ' + str(hex(front)) + rear + '\n'
                file_data += line
        with open(file, "w", encoding="utf-8") as f:
            f.write(file_data)

    def doFive(self):
        self.hook_function = self.multipleParametersWidget.lineEdit_6.text()
        self.syscall_execve_wrapper = self.multipleParametersWidget.lineEdit_5.text()
        self.kernel_start_address = self.multipleParametersWidget.lineEdit.text()
        self.multipleParametersWidget.textBrowser.append('------------------------------')
        # 设置sys_call_table
        self.sys_call_table = self.multipleParametersWidget.lineEdit_2.text()
        self.sys_call_table_change = int(self.sys_call_table ,16) - int(self.kernel_start_address,16) + int(self.kenel_decompressed_address,16)
        self.alter_by_line('./csh/files/step1.s',144,self.sys_call_table_change,' @ syscall: 0xc0030088-0xC0008000+0x3024aa7c   @modify')
        self.multipleParametersWidget.textBrowser.append('sys_call_table设置成功')
        # 设置sys_oabi_call_table
        self.sys_oabi_call_table = self.multipleParametersWidget.lineEdit_3.text()
        self.sys_oabi_call_table_change = int(self.sys_oabi_call_table,16) - int(self.kernel_start_address,16) + int(self.kenel_decompressed_address,16)
        self.alter_by_line('./csh/files/step1.s',145,self.sys_oabi_call_table_change,' @ syscall: 0xc0030704-0xC0008000+0x3024aa7c   @modify')
        self.multipleParametersWidget.textBrowser.append('sys_oabi_call_table设置成功')
        # 设置sys_execve_wrapper
        self.sys_execve_wrapper = int(self.multipleParametersWidget.lineEdit_4.text(),16)
        self.alter_by_line('./csh/files/step2.s',41,self.sys_execve_wrapper,' @sys_execve_wrapper  modify')
        self.multipleParametersWidget.textBrowser.append('sys_execve_wrapper设置成功')
        # 设置syscall_execve_wrapper
        self.syscall_execve_wrapper = int(self.multipleParametersWidget.lineEdit_5.text(),16)
        self.alter_by_line('./csh/files/step3.s', 57, self.syscall_execve_wrapper, ' @syscall_execve_wrapper modify')
        self.multipleParametersWidget.textBrowser.append('syscall_execve_wrapper设置成功')
        # 设置hook_function
        self.hook_function = int(self.multipleParametersWidget.lineEdit_6.text(),16)
        self.alter_by_line('./csh/files/step1.s',147,self.hook_function,'  @ execve 11')
        self.multipleParametersWidget.textBrowser.append('hook_function设置成功')
        item = self.listWidget.item(4)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        item = self.listWidget.item(5)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

    def doSix(self):
        a = subprocess.getstatusoutput('python2 ./csh/files/backdoor.py')
        self.patchWidget.textBrowser.append('----------------------------')
        #print(a)
        self.patchWidget.textBrowser.append(a[1])	


if __name__ == "__main__":
    app = QApplication(sys.argv)
    integrated = Integrated()
    integrated.show()
    sys.exit(app.exec_())
