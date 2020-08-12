#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from unittest import mock
import time

from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt

from PyQt5.QtTest import QTest

sys.path.append("..")

from percentage_ide.tools import json_manager
from percentage_ide import resources

from percentage_ide.core.file_handling import nfile
from percentage_ide.gui.editor import neditable
from percentage_ide.gui.editor.editor import NEditor
from percentage_ide.gui.syntax_registry import syntax_registry  # noqa
from percentage_ide.gui.ide import IDE

json_manager.load_syntax()
themes = json_manager.load_editor_schemes()
resources.COLOR_SCHEME = themes["Percentage Dark"]

qapp = QApplication(sys.argv)
IDE.register_service("ide", mock.Mock())

percentage_editor = NEditor(neditable=neditable.NEditable(nfile.NFile()))
percentage_editor.side_widgets.remove("CodeFoldingWidget")
percentage_editor.side_widgets.remove("MarkerWidget")
percentage_editor.side_widgets.remove("TextChangeWidget")
percentage_editor.side_widgets.update_viewport()
percentage_editor.side_widgets.resize()
percentage_editor.register_syntax_for()
percentage_editor.showMaximized()


click_times = {}

with open(sys.argv[1]) as fp:
    text = fp.read()


def click(key):
    clock_before = time.clock()

    if isinstance(key, str):
        QTest.keyClicks(percentage_editor, key)
    else:
        QTest.keyClick(percentage_editor, key)
    while qapp.hasPendingEvents():
        qapp.processEvents()

    clock_after = time.clock()
    ms = int((clock_after - clock_before) * 100)
    click_times[ms] = click_times.get(ms, 0) + 1


def test():
    clock_before = time.clock()

    for line in text.splitlines():
        indent_width = len(line) - len(line.lstrip())
        while percentage_editor.textCursor().positionInBlock() > indent_width:
            click(Qt.Key_Backspace)
        for i in range(
                indent_width - percentage_editor.textCursor().positionInBlock()):
            click(Qt.Key_Space)

        line = line[indent_width:]
        for char in line:
            click(char)
        click(Qt.Key_Enter)

    clock_after = time.clock()
    typing_time = clock_after - clock_before
    print("Typed {} chars in {} sec. {} ms per character".format(
        len(text), typing_time, typing_time * 1000 / len(text)))
    print("Time per click: Count of clicks")

    click_time_keys = sorted(click_times.keys())
    for click_time_key in click_time_keys:
        print("     %5dms:      %4d" % (
            click_time_key, click_times[click_time_key]))
    qapp.quit()


QTimer.singleShot(0, test)
qapp.exec_()
