
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox
import sys
from pyqt5_CI.ci import CI
from configparser import ConfigParser

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(483, 354)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 20, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")

        self.label_2.setGeometry(QtCore.QRect(40, 80, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 81, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_svnServer = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_svnServer.setGeometry(QtCore.QRect(130, 80, 261, 21))
        self.lineEdit_svnServer.setObjectName("lineEdit_svnServer")
        self.lineEdit_fileLocate = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_fileLocate.setGeometry(QtCore.QRect(130, 120, 261, 21))
        self.lineEdit_fileLocate.setObjectName("lineEdit_fileLocate")
        self.lineEdit_tomcat = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_tomcat.setGeometry(QtCore.QRect(130, 160, 261, 21))
        self.lineEdit_tomcat.setObjectName("lineEdit_tomcat")
        self.checkBox_downloadSVN = QtWidgets.QCheckBox(Dialog)
        self.checkBox_downloadSVN.setGeometry(QtCore.QRect(40, 230, 91, 16))
        self.checkBox_downloadSVN.setObjectName("checkBox_downloadSVN")
        self.checkBox_ant = QtWidgets.QCheckBox(Dialog)
        self.checkBox_ant.setGeometry(QtCore.QRect(130, 230, 71, 16))
        self.checkBox_ant.setObjectName("checkBox_ant")
        self.checkBox_dploy = QtWidgets.QCheckBox(Dialog)
        self.checkBox_dploy.setGeometry(QtCore.QRect(220, 230, 71, 16))
        self.checkBox_dploy.setObjectName("checkBox_dploy")
        self.checkBox_startTest = QtWidgets.QCheckBox(Dialog)
        self.checkBox_startTest.setGeometry(QtCore.QRect(310, 230, 71, 16))
        self.checkBox_startTest.setObjectName("checkBox_startTest")
        self.pushButton_start = QtWidgets.QPushButton(Dialog)
        self.pushButton_start.setGeometry(QtCore.QRect(70, 280, 75, 23))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_save = QtWidgets.QPushButton(Dialog)
        self.pushButton_save.setGeometry(QtCore.QRect(320, 280, 75, 23))
        self.pushButton_save.setObjectName("pushButton_save")
        self.checkBox_sendReport = QtWidgets.QCheckBox(Dialog)
        self.checkBox_sendReport.setGeometry(QtCore.QRect(390, 230, 71, 16))
        self.checkBox_sendReport.setObjectName("checkBox_sendReport")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "欢迎使用woniucbt持续集成框架"))
        self.label_2.setText(_translate("Dialog", "SVN服务地址"))
        self.label_3.setText(_translate("Dialog", "File地址"))
        self.label_4.setText(_translate("Dialog", "Tomcat地址"))
        self.checkBox_downloadSVN.setText(_translate("Dialog", "下载源码"))
        self.checkBox_ant.setText(_translate("Dialog", "构建版本"))
        self.checkBox_dploy.setText(_translate("Dialog", "部署系统"))
        self.checkBox_startTest.setText(_translate("Dialog", "执行测试"))
        self.pushButton_start.setText(_translate("Dialog", "开始测试"))
        self.pushButton_save.setText(_translate("Dialog", "保存配置"))
        self.checkBox_sendReport.setText(_translate("Dialog", "发送报告"))

from pyqt5_CI.ci import CI
class WonniuCI(QWidget,Ui_Dialog):
    def __init__(self):
        super(WonniuCI,self).__init__()
        self.setupUi(self)

        self.wc =CI()
    def get_config(self,section,key):
        config=ConfigParser()
        config.read('./ci.conf')
        return config.get(section,key)
    def test_choice(self):
        # ui = Ui_Dialog()
        print('1111111111111111111111')
        if self.checkBox_downloadSVN.isChecked():
            print('2222222222')
            self.wc.download_svn()
        if self.checkBox_ant.isChecked():
            self.wc.ant_compile()
        if self.checkBox_dploy.isChecked():
            self.wc.deploy()
        # if ui.checkBox_startTest:


    def save_config(self):
        file_path=self.ui.lineEdit_fileLocate.text()
        svn_url=self.ui.lineEdit_svnServer.text()
        tomcat=self.ui.lineEdit_tomcat.text()
        config=ConfigParser()
        config.set('ci','file_path',file_path)
        config.set('ci','svn_url',svn_url)
        config.set('ci','tomcat',tomcat)

    # def start_test(self):
if __name__ == '__main__':
    app=QApplication(sys.argv)
    qtCI=WonniuCI()
    qtCI.show()

    qtCI.pushButton_start.clicked.connect(qtCI.test_choice)
    qtCI.pushButton_save.clicked.connect(qtCI.save_config)

    sys.exit(app.exec())