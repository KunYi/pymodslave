#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      elbar
#
# Created:     28/08/2012
# Copyright:   (c) elbar 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from PyQt4 import QtGui,QtCore
from Ui_mbdata import Ui_MBData
from ModSlaveMBDataModel import ModSlaveMBDataModel

#-------------------------------------------------------------------------------
class ModSlaveMBDataWindow(QtGui.QMainWindow):
    """ Class wrapper for modbus data """

    def __init__(self):
        super(ModSlaveMBDataWindow,self).__init__()
        #data models
        self.coils = None
        self.dis_inputs = None
        self.input_regs = None
        self.hold_regs = None
        #setu UI
        self.setupUI()

    def setupUI(self):
        #create window from ui
        self.ui=Ui_MBData()
        self.ui.setupUi(self)
        #signals-slots
        self.ui.chkSimCoils.stateChanged.connect(self._sim_coils_changed)
        self.ui.chkSimDisInputs.stateChanged.connect(self._sim_dis_inputs_changed)
        self.ui.chkSimInputRegs.stateChanged.connect(self._sim_input_regs_changed)
        self.ui.chkSimHoldRegs.stateChanged.connect(self._sim_hold_regs_changed)
        self.ui.cmbInputRegsType.currentIndexChanged.connect(self._input_regs_data_type_changed)
        self.ui.cmbHoldRegsType.currentIndexChanged.connect(self._hold_regs_data_type_changed)
        #read only table views
        self.ui.tvCoilsData.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.tvDiscreteInputsData.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.tvHoldingRegistersData.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.tvInputRegistersData.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

    def set_data_models(self, coils, dis_inputs, input_regs, hold_regs):
        self.coils = coils
        self.dis_inputs = dis_inputs
        self.input_regs = input_regs
        self.hold_regs = hold_regs
        #table views models
        #coils
        self.ui.tvCoilsData.setModel(self.coils.model)
        self.coils.model.dataChanged.connect(self._models_data_changed)
        self._sim_coils_changed()
        #discrete inputs
        self.ui.tvDiscreteInputsData.setModel(self.dis_inputs.model)
        self.dis_inputs.model.dataChanged.connect(self._models_data_changed)
        self._sim_dis_inputs_changed()
        #input regs
        self.ui.tvInputRegistersData.setModel(self.input_regs.model)
        self.input_regs.model.dataChanged.connect(self._models_data_changed)
        self.input_regs.set_data_type(self.ui.cmbInputRegsType.currentIndex())
        self._sim_input_regs_changed()
        #holding regs
        self.ui.tvHoldingRegistersData.setModel(self.hold_regs.model)
        self.hold_regs.model.dataChanged.connect(self._models_data_changed)
        self.hold_regs.set_data_type(self.ui.cmbHoldRegsType.currentIndex())
        self._sim_hold_regs_changed()
        #update table views
        self._models_data_changed()

    def _sim_coils_changed(self):
        self.coils.sim = self.ui.chkSimCoils.isChecked()

    def _sim_dis_inputs_changed(self):
        self.dis_inputs.sim = self.ui.chkSimDisInputs.isChecked()

    def _sim_input_regs_changed(self):
        self.input_regs.sim = self.ui.chkSimInputRegs.isChecked()

    def _sim_hold_regs_changed(self):
        self.hold_regs.sim = self.ui.chkSimHoldRegs.isChecked()

    def _models_data_changed(self):
        self.ui.tvCoilsData.resizeColumnsToContents()
        self.ui.tvDiscreteInputsData.resizeColumnsToContents()
        self.ui.tvInputRegistersData.resizeColumnsToContents()
        self.ui.tvHoldingRegistersData.resizeColumnsToContents()

    def _input_regs_data_type_changed(self):
        if (self.input_regs):
            self.input_regs.set_data_type(self.ui.cmbInputRegsType.currentIndex())

    def _hold_regs_data_type_changed(self):
        if (self.hold_regs):
            self.hold_regs.set_data_type(self.ui.cmbHoldRegsType.currentIndex())

#-------------------------------------------------------------------------------