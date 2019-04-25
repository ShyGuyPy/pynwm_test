#from suds.client import Client
from traceback import format_exc
import sys
#import FEWSConnect
import logging
from paramiko import Transport
from paramiko import SFTPClient

if (__name__ == '__main__'):
    host = "ftp.ncep.noaa.gov"
    port = 22 #after much testing....port 22 is the place to be
    #usr = "cschultz"
    #pw = "Shenandoah22"
    path = "/pub/data/nccf/com/nwm/prod/"#r"/Distribution/RHA-Data/rhapub5/hefs_icprb"
    lookback = 5

    #ftp://ftp.ncep.noaa.gov/pub/data/nccf/com/nwm/prod

    #https://ftp.ncep.noaa.gov/data/nccf/com/nwm/prod/

    # try:
    #     transport = Transport((host, port))
    #     transport.connect()#username = usr, password = pw)
    #     sftp = SFTPClient.from_transport(transport)
    #     print("1 it's alive...sftp object up and running")
    # except:
    #     print("1 failed to connect")

    transport = Transport((host, port))
    transport.connect()#username = usr, password = pw)
    sftp = SFTPClient.from_transport(transport)