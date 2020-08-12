# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from PyQt5.QtCore import (
    QSettings,
    pyqtSignal
)


class NSettings(QSettings):
    """Extend QSettings to emit a signal when a value change."""

    valueChanged = pyqtSignal("QString", "PyQt_PyObject")

    def __init__(self, path, fformat=QSettings.IniFormat):
        super().__init__(path, fformat)

    def setValue(self, key, value):
        super().setValue(key, value)
        self.valueChanged.emit(key, value)


'''class NSettings(QSettings):

    """
    Extend QSettings to emit a signal when a value change.
    @signals:
    valueChanged(QString, PyQt_PyObject)
    """
    valueChanged = pyqtSignal('PyQt_PyObject', 'QString', 'PyQt_PyObject')

    def __init__(self, path, obj=None, fformat=QSettings.IniFormat, prefix=''):
        super(NSettings, self).__init__(path, fformat)
        self.__prefix = prefix
        self.__object = obj

    def setValue(self, key, value):
        super(NSettings, self).setValue(key, value)
        key = "%s_%s" % (self.__prefix, key)
        self.valueChanged.emit(self.__object, key, value)
'''