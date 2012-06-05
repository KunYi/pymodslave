#-------------------------------------------------------------------------------
# Name:        ModSlaveSettings
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
from Ui_settings import Ui_Settings

#-------------------------------------------------------------------------------
class ModSlaveSettingsWindow(QtGui.QDialog):
    """ Class wrapper for general settings ui """

    def __init__(self):
        super(ModSlaveSettingsWindow,self).__init__()
        #init values
        self.coils = 50
        self.inputs = 50
        self.input_regs = 50
        self.hold_regs = 50
        self.setupUI()

    def setupUI(self):
        #create window from ui
        self.ui=Ui_Settings()
        self.ui.setupUi(self)
        #set init values
        self._set_values()
        #signals-slots
        self.accepted.connect(self._OK_pressed)
        self.rejected.connect(self._cancel_pressed)

    def _set_values(self):
        """set param values to ui"""
        self.ui.sbNoOfCoils.setValue(self.coils)
        self.ui.sbNoOfDigInputs.setValue(self.inputs)
        self.ui.sbNoOfInputRegs.setValue(self.input_regs)
        self.ui.sbNoOfHoldingRegs.setValue(self.hold_regs)

    def _get_values(self):
        """get param values from ui"""
        self.coils = self.ui.sbNoOfCoils.value()
        self.inputs = self.ui.sbNoOfDigInputs.value()
        self.input_regs = self.ui.sbNoOfInputRegs.value()
        self.hold_regs = self.ui.sbNoOfHoldingRegs.value()

    def _OK_pressed(self):
        """new values are accepted"""
        self._get_values()

    def _cancel_pressed(self):
        """new values are rejected"""
        self._set_values()
#-------------------------------------------------------------------------------