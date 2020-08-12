# -*- coding: utf-8 -*-
 
from PyQt5.QtCore import QObject

from percentage_ide.gui.ide import IDE


class PluginsManager(QObject):

    def __init__(self):
        super(PluginsManager, self).__init__()

    def get_activated_plugins(self):
        qsettings = IDE.percentage_settings()
        return qsettings.value('plugins/registry/activated', [])

    def get_failstate_plugins(self):
        qsettings = IDE.percentage_settings()
        return qsettings.value('plugins/registry/failure', [])

    def get_to_activate_plugins(self):
        qsettings = IDE.percentage_settings()
        return qsettings.value('plugins/registry/toactivate', [])

    def set_to_activate_plugins(self, to_activate):
        qsettings = IDE.percentage_settings()
        qsettings.setValue('plugins/registry/toactivate', to_activate)

    def set_activated_plugins(self, activated):
        qsettings = IDE.percentage_settings()
        qsettings.setValue('plugins/registry/activated', activated)

    def set_failstate_plugins(self, failure):
        qsettings = IDE.percentage_settings()
        qsettings.setValue('plugins/registry/failure', failure)

    def activate_plugin(self, plugin):
        """
        Receives PluginMetadata instance and activates its given plugin
        BEWARE: We do not do any kind of checking about if the plugin is
        actually installed.
        """
        plugin_name = plugin.name
        to_activate = self.get_to_activate_plugins()
        to_activate.append(plugin_name)
        self.set_to_activate_plugins(to_activate)
        self.__activate_plugin(plugin, plugin_name)

    def load_all_plugins(self):
        to_activate = self.get_to_activate_plugins()
        for each_plugin in to_activate:
            self.__activate_plugin(__import__(each_plugin), each_plugin)

    def __activate_plugin(self, plugin, plugin_name):
        """
        Receives the actual plugin module and tries activate or marks
        as failure
        """
        activated = self.get_activated_plugins()
        failure = self.get_failstate_plugins()

        try:
            plugin.activate()
        except Exception:
            # This plugin can no longer be activated
            if plugin_name in activated:
                activated.remove(plugin_name)
            if plugin_name not in failure:
                failure.append(plugin_name)
        else:
            activated.append(plugin_name)
            if plugin_name in failure:
                failure.remove(plugin_name)
        finally:
            self.set_activated_plugins(activated)
            self.set_failstate_plugins(failure)
