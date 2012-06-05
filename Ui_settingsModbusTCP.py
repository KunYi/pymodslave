# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Projects\python\pyModSlaveQt\ui\settingsmodbustcp.ui'
#
# Created: Wed Apr 18 10:08:28 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SettingsModbusTCP(object):
    def setupUi(self, SettingsModbusTCP):
        SettingsModbusTCP.setObjectName(_fromUtf8("SettingsModbusTCP"))
        SettingsModbusTCP.resize(180, 80)
        SettingsModbusTCP.setMinimumSize(QtCore.QSize(180, 80))
        SettingsModbusTCP.setMaximumSize(QtCore.QSize(180, 80))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/network-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SettingsModbusTCP.setWindowIcon(icon)
        SettingsModbusTCP.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(SettingsModbusTCP)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.leTCPPort = QtGui.QLineEdit(SettingsModbusTCP)
        self.leTCPPort.setObjectName(_fromUtf8("leTCPPort"))
        self.gridLayout.addWidget(self.leTCPPort, 0, 1, 1, 1)
        self.lblTCPPort = QtGui.QLabel(SettingsModbusTCP)
        self.lblTCPPort.setObjectName(_fromUtf8("lblTCPPort"))
        self.gridLayout.addWidget(self.lblTCPPort, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(SettingsModbusTCP)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.lblTCPPort.setBuddy(self.leTCPPort)

        self.retranslateUi(SettingsModbusTCP)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SettingsModbusTCP.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SettingsModbusTCP.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsModbusTCP)

    def retranslateUi(self, SettingsModbusTCP):
        SettingsModbusTCP.setWindowTitle(QtGui.QApplication.translate("SettingsModbusTCP", "Modbus TCP Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.leTCPPort.setText(QtGui.QApplication.translate("SettingsModbusTCP", "502", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTCPPort.setText(QtGui.QApplication.translate("SettingsModbusTCP", "TCP Port", None, QtGui.QApplication.UnicodeUTF8))

import pyModSlaveQt_rc
