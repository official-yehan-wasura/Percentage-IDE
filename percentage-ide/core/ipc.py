# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os

from PyQt5.QtNetwork import QLocalSocket


file_delimiter = '<-nf>'
project_delimiter = '<-np>'


def is_running():
    local_socket = QLocalSocket()
    local_socket.connectToServer("percentage_ide")
    if local_socket.state():
        # It's running
        result = (True, local_socket)
    else:
        # It's not running
        result = (False, local_socket)
    return result


def send_data(socket, filenames, projects_path, linenos):
    global file_delimiter
    global project_delimiter
    file_with_nro = ['%s:%i' % (os.path.abspath(f[0]), f[1] - 1)
                     for f in zip(filenames, linenos)]
    file_without_nro = ['%s:%i' % (os.path.abspath(f), 0)
                        for f in filenames[len(linenos):]]
    filenames = file_with_nro + file_without_nro
    files = file_delimiter.join(filenames)
    projects = project_delimiter.join(projects_path)
    data = files + project_delimiter + projects
    data_sended = False
    try:
        result = socket.write(data)
        socket.flush()
        socket.close()
        if result >= 0:
            data_sended = True
    except:
        data_sended = False
    return data_sended
