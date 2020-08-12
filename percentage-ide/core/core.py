# -*- coding: utf-8 -*-

import sys
import os
import signal

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QCoreApplication

from percentage_ide.core import cliparser

PR_SET_NAME = 15
PROCNAME = b"percentage-ide"


def run_percentage():
    """First obtain the execution args and create the resources folder."""
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    # Change the process name only for linux yet
    is_linux = sys.platform == "darwin" or sys.platform == "win32"
    if is_linux:
        try:
            import ctypes
            libc = ctypes.cdll.LoadLibrary('libc.so.6')
            # Set the application name
            libc.prctl(PR_SET_NAME, b"%s\0" % PROCNAME, 0, 0, 0)
        except OSError:
            print("The process couldn't be renamed'")
    filenames, projects_path, extra_plugins, linenos, log_level, log_file = \
        cliparser.parse()
    # Create the QApplication object before using the
    # Qt modules to avoid warnings
    app = QApplication(sys.argv)
    from percentage_ide import resources
    from percentage_ide.core import settings
    resources.create_home_dir_structure()
    # Load Logger
    from percentage_ide.tools.logger import PercentageLogger
    PercentageLogger.argparse(log_level, log_file)

    # Load Settings
    settings.load_settings()
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling, settings.HDPI)
    if settings.CUSTOM_SCREEN_RESOLUTION:
        os.environ["QT_SCALE_FACTOR"] = settings.CUSTOM_SCREEN_RESOLUTION
    from percentage_ide import percentage_style
    app.setStyle(percentage_style.PercentageStyle(resources.load_theme()))

    from percentage_ide import gui
    # Start the UI
    gui.start_ide(app, filenames, projects_path, extra_plugins, linenos)

    sys.exit(app.exec_())
