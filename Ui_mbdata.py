# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mbdata.ui'
#
# Created: Thu Nov 12 20:31:33 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MBData(object):
    def setupUi(self, MBData):
        MBData.setObjectName(_fromUtf8("MBData"))
        MBData.resize(500, 420)
        MBData.setMinimumSize(QtCore.QSize(500, 420))
        MBData.setMaximumSize(QtCore.QSize(500, 420))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/Bus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MBData.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MBData)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MBData.setCentralWidget(self.centralwidget)

        self.retranslateUi(MBData)
        QtCore.QMetaObject.connectSlotsByName(MBData)

    def retranslateUi(self, MBData):
        MBData.setWindowTitle(_translate("MBData", "Data", None))

import pyModSlaveQt_rc
