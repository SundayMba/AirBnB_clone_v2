#!/usr/bin/python3
# Compress before sending using tar gzipped algorithm
import os
from fabric import task
from datetime import datetime

@task
def do_pack(c):
    """ Create a tar gzipped archived of the directory web_static """

    # create a versions folder if it does not exist
    if not os.path.exists("versions"):
        if c.run("mkdir versions").failed:
            return None
    dt = datetime.utcnow()
    timestamp = dt.strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)
    if c.run("tar -cvzf {} web_static".format(archive_name)).failed:
        return None
    return archive_name

