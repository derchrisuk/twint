import datetime

import logging as logme

class Datelock:
    _until = None
    _since = None
    _since_def_user = None

def Set(Until, Since):
    logme.debug(__name__+':Set')
    d = Datelock()

    if Until:
        d._until = datetime.datetime.strptime(Until, "%Y-%m-%d %H:%M:%S").date()
    else:
        d._until = datetime.date.today()

    if Since:
        d._since = datetime.datetime.strptime(Since, "%Y-%m-%d %H:%M:%S").date()
        d._since_def_user = True
    else:
        d._since = datetime.datetime.strptime("2006-03-21 12:00:00", "%Y-%m-%d %H:%M:%S").date()
        d._since_def_user = False

    return d
