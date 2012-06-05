#-------------------------------------------------------------------------------
# Name:        ModSlaveAbout
# Purpose:
#
# Author:      ElBar
#
# Created:     17/04/2012
# Copyright:   (c) ElBar 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from PyQt4 import QtGui,QtCore
from Ui_about import Ui_About

_VERSION = "0.3.0"

#-------------------------------------------------------------------------------
class ModSlaveAboutWindow(QtGui.QDialog):
    """ Class wrapper for about window ui """

    def __init__(self):
        super(ModSlaveAboutWindow,self).__init__()
        self.setupUI()

    def setupUI(self):
        #create window from ui
        self.ui=Ui_About()
        self.ui.setupUi(self)
        self.ui.lblVersion.setText("pyModSlave v{0}".format(_VERSION))
#-------------------------------------------------------------------------------