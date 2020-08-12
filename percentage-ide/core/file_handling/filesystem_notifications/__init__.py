# -*- coding: utf-8 -*-
 
from __future__ import absolute_import

import sys

try:
    if sys.platform == 'win32':
        from percentage_ide.core.file_handling.filesystem_notifications import windows
        source = windows
    elif sys.platform == 'darwin':
        from percentage_ide.core.file_handling.filesystem_notifications import darwin
        source = darwin
    elif sys.platform.startswith("linux"):
        from percentage_ide.core.file_handling.filesystem_notifications import linux
        source = linux
    else:
        #Aything we do not have a clue how to handle
        from percentage_ide.core.file_handling.filesystem_notifications import openbsd
        source = openbsd
except:
    from percentage_ide.core.file_handling.filesystem_notifications import openbsd
    source = openbsd


PercentageFileSystemWatcher = source.PercentageFileSystemWatcher()
