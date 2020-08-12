# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
import sys

from PyQt4.QtCore import QObject

from percentage_ide.tools.logger import PercentageLogger


class Plugin(QObject):
    '''
    Base class for ALL Plugin
    All plugins should inherit from this class
    '''

    def __init__(self, locator, metadata=None):
        QObject.__init__(self)
        self.locator = locator
        if metadata is None:
            self.metadata = {}
        else:
            self.metadata = metadata
        klass = self.__class__
        plugin_name = "%s.%s" % (klass.__module__, klass.__name__)
        self.logger = PercentageLogger('percentage_ide.plugins.%s' % plugin_name)
        #set the path!
        try:
            self_module = self.__module__
            path = os.path.abspath(sys.modules[self_module].__file__)
            self._path = os.path.dirname(path)
        except:
            self._path = ''

    def initialize(self):
        """The initialization of the Plugin should be here."""
        self.logger.info("Initializing Plugin...")

    def finish(self):
        pass

    def get_preferences_widget(self):
        pass

    @property
    def path(self):
        return self._path
