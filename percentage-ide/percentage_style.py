# -*- coding: utf-8 -*-
import os

from PyQt5.QtWidgets import QProxyStyle
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QStyleFactory
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QColor

from percentage_ide import resources


class PercentageStyle(QProxyStyle):

    def __init__(self, theme):
        QProxyStyle.__init__(self)
        self.setBaseStyle(QStyleFactory.create("fusion"))
        self._palette = theme["palette"]
        self._qss = theme["stylesheet"]

    def polish(self, args):
        if isinstance(args, QPalette):
            palette = args
            for role, color in self._palette.items():
                qcolor = QColor(color)
                color_group = QPalette.All
                if role.endswith("Disabled"):
                    role = role.split("Disabled")[0]
                    color_group = QPalette.Disabled
                elif role.endswith("Inactive"):
                    role = role.split("Inactive")[0]
                    qcolor.setAlpha(90)
                    color_group = QPalette.Inactive
                color_role = getattr(palette, role)
                palette.setBrush(color_group, color_role, qcolor)
        elif isinstance(args, QApplication):
            # Set style sheet
            filename = os.path.join(resources.PERCENTAGE_QSS, self._qss)
            with open(filename + ".qss") as fileaccess:
                qss = fileaccess.read()
            args.setStyleSheet(qss)
        return QProxyStyle.polish(self, args)
