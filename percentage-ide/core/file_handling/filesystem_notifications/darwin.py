# -*- coding: utf-8 -*-
 
from __future__ import absolute_import

#import fsevents
#from PyQt4.QtCore import SIGNAL

from percentage_ide.tools.logger import PercentageLogger
logger = PercentageLogger('percentage_ide.core.file_handling.filesystem_notifications.darwin')
DEBUG = logger.debug

from percentage_ide.core.file_handling.filesystem_notifications import base_watcher
ADDED = base_watcher.ADDED
DELETED = base_watcher.DELETED
REMOVE = base_watcher.REMOVE
RENAME = base_watcher.RENAME
MODIFIED = base_watcher.MODIFIED


class PercentageFileSystemWatcher(base_watcher.BaseWatcher):

    def __init__(self):
        super(PercentageFileSystemWatcher, self).__init__()
        #self.observer = fsevents.Observer()
        #self.watching_paths = {}
        #self.event_mapping = {
            #fsevents.IN_CREATE: ADDED,
            #fsevents.IN_MODIFY: MODIFIED,
            #fsevents.IN_DELETE: DELETED,
            #fsevents.IN_MOVED_FROM: REMOVE,
            #fsevents.IN_MOVED_TO: ADDED}

    def shutdown_notification(self):
        pass
        #base_watcher.BaseWatcher.shutdown_notification(self)
        #try:
            #for path in self.watching_paths:
                #stream = self.watching_paths[path]
                #self.observer.unschedule(stream)
        #except:
            #logger.debug("Some of the stream could not be unscheduled.")
        #self.observer.stop()
        #self.observer.join()

    def add_watch(self, path):
        pass
        #if path not in self.watching_paths:
            #try:
                #if isinstance(path, unicode):
                    #path = path.encode('utf-8')
                #stream = fsevents.Stream(self._emit_signal_on_change,
                    #path, file_events=True)
                #self.observer.schedule(stream)
                #self.watching_paths[path] = stream
                #if not self.observer.is_alive():
                    #self.observer.start()
            #except Exception as reason:
                #print reason
                #logger.debug("Path could not be added: %r" % path)

    def remove_watch(self, path):
        pass
        #try:
            #if path in self.watching_paths:
                #stream = self.watching_paths[path]
                #self.observer.unschedule(stream)
                #self.watching_paths.remove(path)
                #self.observer.join()
                #if not self.observer.is_alive():
                    #self.observer = fsevents.Observer()
        #except:
            #logger.debug("Stream could not be removed for path: %r" % path)

    def _emit_signal_on_change(self, event):
        pass
        #oper = self.event_mapping.get(event.mask, None)
        #if oper is None:
            #return
        #path = event.name
        #self.emit(SIGNAL("fileChanged(int, QString)"), oper, path)
