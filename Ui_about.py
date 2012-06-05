# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Projects\python\pyModSlaveQt\ui\about.ui'
#
# Created: Mon Apr 23 13:17:09 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.resize(400, 80)
        About.setMaximumSize(QtCore.QSize(400, 80))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/info16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About.setWindowIcon(icon)
        About.setModal(True)
        self.horizontalLayout = QtGui.QHBoxLayout(About)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblVersion = QtGui.QLabel(About)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblVersion.setFont(font)
        self.lblVersion.setAlignment(QtCore.Qt.AlignCenter)
        self.lblVersion.setObjectName(_fromUtf8("lblVersion"))
        self.horizontalLayout.addWidget(self.lblVersion)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(QtGui.QApplication.translate("About", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.lblVersion.setText(QtGui.QApplication.translate("About", "pyModSlave", None, QtGui.QApplication.UnicodeUTF8))

import pyModSlaveQt_rc
