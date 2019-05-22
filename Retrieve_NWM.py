


from bs4 import BeautifulSoup
import requests
import wget
from datetime import datetime, timedelta

date_today = datetime.today().strftime('%Y%m%d')
date_yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d')

#the http site for NWM products
site_path = 'https://www.ftp.ncep.noaa.gov/data/nccf/com/nwm/prod/nwm.'


data_range = '/short_range/'

#creates a url to pull yesterdays data
url = site_path+date_yesterday+data_range

#netcdf extension
ext = 'nc'

#creates list of url directory content
def listFD(url, ext=''):
    page = requests.get(url).text
    #print page
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

test_list = []

#finds the last hour that data was recorded.  should be 23
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

#append data found at last hour of day to a separate list
for file in listFD(url, ext):
    if file.find(max_hour+".short_range.channel") >1: #& file.find("t17z") >1 :
        test_list.append(file)

#sloppy naming convention...this downloads the data to a designated directory
count = 0
for file in test_list:
    count = count +1
    test_url = str(file)
    wget.download(test_url, '/Users/icprbadmin/Documents/Python_Scripts/NWM/data/5_21_2019/test/'+str(date_yesterday)+'test_data'+str(count)+'.nc')
