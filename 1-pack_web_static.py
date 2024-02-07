#!/usr/bin/python3
# Compress before sending using tar gzipped algorithm
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Create a tar gzipped archived of the directory web_static """

    # create a versions folder if it does not exist
    if not os.path.exists("versions"):
        if local("mkdir versions").failed:
            return None
    dt = datetime.utcnow()
    timestamp = dt.strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)
    if local("tar -cvzf {} web_static".format(archive_name)).failed:
        return None
    return archive_name
