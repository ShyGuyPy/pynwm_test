from traceback import format_exc
import sys
#import FEWSConnect
import logging
from paramiko import Transport
from paramiko import SFTPClient
import os
import stat
import paramiko





host = 'www.ftp.ncep.noaa.gov'
site_path = '/data/nccf/com/nwm/prod/nwm.20190515/short_range/'

#host = 'ftp://ftp.ncep.noaa.gov'
#site_path = '/pub/data/nccf/com/nwm/prod/nwm.20190515/short_range/'

port = 21  # after much testing....port 22 is the place to be

lookback = 5

destination = r"C:\Users\Public\Documents\Python Scripts\file_destination"
file_name = 'nwm.t00z.short_range.channel_rt.f001.conus.nc'

importDir = "C:/Users/Public/Documents/Python Scripts/file_destination"  # open(destination + file_name + extension, "wb")





#Use requests to get page content and BeautifulSoup to parse the result.
#For example if we search for all iso files at http://cdimage.debian.org/debian-cd/8.2.0-live/i386/iso-hybrid/:

from bs4 import BeautifulSoup
import requests
import wget
from datetime import datetime

date_today = datetime.today().strftime('%Y%m%d')

site_path = 'https://www.ftp.ncep.noaa.gov/data/nccf/com/nwm/prod/nwm.'


data_range = '/short_range/'

file = 'nwm.t00z.short_range.channel_rt.f001.conus.nc'

url = site_path+date_today+data_range

ext = 'nc'

def listFD(url, ext=''):
    page = requests.get(url).text
    #print page
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

test_list = []

for file in listFD(url, ext):
    if file.find("t23z.short_range.channel") >1: #& file.find("t17z") >1 :
        max_hour = "t23z"
    elif file.find("t22z.short_range.channel") >1: #& file.find("t17z") >1 :
        max_hour = "t22z"
    elif file.find("t21z.short_range.channel") >1: #& file.find("t17z") >1 :
        max_hour = "t21z"
    elif  file.find("t20z.short_range.channel") >1: #& file.find("t17z") >1 :
        max_hour = "t20z"
    elif  file.find("t19z.short_range.channel") >1: #& file.find("t17z") >1 :
        max_hour = "t19z"
    elif  file.find("t18z.short_range.channel") >1: #& file.find("t17z") >1 :
        max_hour = "t18z"
    elif  file.find("t17z.short_range.channel") >1: #& file.find("t17z") >1 :
        max_hour = "t17z"



print(max_hour)

for file in listFD(url, ext):
    #print file
    if file.find(max_hour+".short_range.channel") >1: #& file.find("t17z") >1 :
        test_list.append(file)

#print(test_list)
count = 0
for file in test_list:
    count = count +1
    test_url = str(test_list)
    print(test_url)
    print('/Users/icprbadmin/Documents/Python_Scripts/NWM/data/5_21_2019/test/'+str(date_today)+'test_data'+str(count)+'.nc')
    wget.download(test_url, '/Users/icprbadmin/Documents/Python_Scripts/NWM/data/5_21_2019/test/'+str(date_today)+'test_data'+str(count)+'.nc')

#url = 'https://www.ftp.ncep.noaa.gov/data/nccf/com/nwm/prod/nwm.20190521/short_range/nwm.t00z.short_range.channel_rt.f001.conus.nc'
#wget.download(test_url, '/Users/icprbadmin/Documents/Python_Scripts/NWM/data/5_21_2019/test/test.nc')

# 1
#try:

# transport = Transport((host, port))
# transport.connect()
# sftp = SFTPClient.from_transport(transport)
# print("1 it's alive...sftp object up and running")
# except:
#     print("1 failed to connect")



#
#
#
# # 2
# try:
#     # Retrieve list of files from sftp site
#     s = sftp.listdir(site_path)
#     # print("2 These are the files in " + host )#+ path + ": ")
#     # print(s)
# except:
#     print("2 no good retrieving file list")
# #
# # t=sftp.listdir(path)
# # 3
# try:
#     hrsback = int(lookback) * 24
#     # List of files in directory
#     allfiles = [filename for filename in s if filename.endswith('.txt')][-hrsback:]
#     print('3' + allfiles)
# except:
#     print("3 no good finding file")
# # 4
# try:
#     for file in allfiles:
#         reader = sftp.open(site_path + file, 'rb').read()
#         # print(pdf)
#         print("4 read successful")
#
# except:
#     print("4 no good on read from file")
#
# # 5
# try:
#     for file in allfiles:
#         #        Store file in FEWS import Directory
#         with open(importDir + file, 'wb') as f:
#             f.write(reader)
#     print("5 file saved to " + importDir + file)
# except:
#     print("5 no good on file save attempt 1")
#     # print(pdf)
# # 6
# try:
#     sftp.close()
#     print("6 closed sftp object")
# except:
#     print("6 sftp did not close")
# # 7
# try:
#     f.close()  # importDir.close()
#     print("7 closed importDir object")
# except:
#     print("7 importDir did not close")