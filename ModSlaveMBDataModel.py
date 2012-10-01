#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      elbar
#
# Created:     29/08/2012
# Copyright:   (c) elbar 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from PyQt4 import QtGui,QtCore

#-------------------------------------------------------------------------------
class ModSlaveMBDataModel(object):

    def __init__(self, no_of_items = 10, data_type = 0):#data type > 0 : decimal, 1 : hex
        self.__no_of_items = no_of_items
        self.__no_of_model_items = ((no_of_items - 1) // 10 + 1) * 10
        self.model = QtGui.QStandardItemModel((no_of_items - 1) // 10 + 1, 10)
        self.model.setHorizontalHeaderLabels(("0","1","2","3","4","5","6","7","8","9"))
        self.model.setVerticalHeaderLabels(["%02d"%(x*10) for x in range((no_of_items - 1) // 10 + 1)])
        self._data = None
        self._data_type = data_type
        #simulate values
        self.sim = False

    def update_model(self, data):
        self._data = data
        for i in range(self.__no_of_model_items):
            row = i //10
            col = i % 10
            idx = self.model.index(row, col, QtCore.QModelIndex())
            if (i >= self.__no_of_items):#not used cells
                self.model.setData(idx, "x", QtCore.Qt.DisplayRole)
                self.model.setData(idx, QtGui.QBrush(QtCore.Qt.red), QtCore.Qt.ForegroundRole)
                self.model.setData(idx, QtGui.QBrush(QtCore.Qt.lightGray), QtCore.Qt.BackgroundRole)
                item = self.model.itemFromIndex(idx)
                item.setEditable(False)
            else:
                if (self._data_type == 0):#decimal
                    self.model.setData(idx, self._data[i], QtCore.Qt.DisplayRole)
                    self.model.setData(idx, "Address : {0}".format(i), QtCore.Qt.ToolTipRole)
                else:#hex
                    self.model.setData(idx,"%X"%self._data[i], QtCore.Qt.DisplayRole)

    def set_data_type(self, dt):
        self._data_type = dt
        self.update_model(self._data)

#-------------------------------------------------------------------------------