# -*- coding: utf-8 -*-

from __future__ import absolute_import


###############################################################################
# METADATA
###############################################################################

__prj__ = "PERCENTAGE-IDE"
__author__ = "Yehan Wasura"
__mail__ = "contact@yehanwasura.ml"
__url__ = "http://www.percentage-ide.org"
__source__ = "https://github.com/percentage-ide/percentage-ide"
__version__ = "2.0-alpha"
__license__ = "GPL3"

###############################################################################
# DOC
###############################################################################

"""PERCENTAGE-IDE is a cross-platform integrated development environment (IDE).
PERCENTAGE-IDE runs on Linux/X11, Mac OS X and Windows desktop operating systems,
and allows developers to create applications for several purposes using all the
tools and utilities of PERCENTAGE-IDE, making the task of writing software easier
and more enjoyable.
"""

###############################################################################
# SET PYQT API 2
###############################################################################

# import sip
# API_NAMES = ["QDate", "QDateTime", "QString", "QTime", "QUrl", "QTextStream",
#             "QVariant"]
# API_VERSION = 2
# for name in API_NAMES:
#    sip.setapi(name, API_VERSION)

###############################################################################
# START
###############################################################################


def setup_and_run():
    """Load the Core module and trigger the execution."""
    # import only on run
    # Dont import always this, setup.py will fail
    from percentage_ide import core
    from percentage_ide import nresources  # noqa
    from multiprocessing import freeze_support

    # Used to support multiprocessing on windows packages
    freeze_support()

    # Run PERCENTAGE-IDE
    core.run_percentage()
