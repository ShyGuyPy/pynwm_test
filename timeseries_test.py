from pathlib import Path
import os

import netCDF4
import dateutil
import pytz
from bs4 import BeautifulSoup

from pynwm import nwm_data, nwm_subset

import numpy as np
import matplotlib.pyplot as plt

file_list_1239 = []
file_list_1340 = []

test = []
test2= []
test3 = []
test4 = []
test5 = []
test6 = []

#Point of Rocks
comids =[4507344]

path_1239 = 'C:/Users/icprbadmin/Documents/Python_Scripts/NWM/data/5_13_2019/12_39/'
path_1340 = 'C:/Users/icprbadmin/Documents/Python_Scripts/NWM/data/5_13_2019/13_40/'
path_1442 = 'C:/Users/icprbadmin/Documents/Python_Scripts/NWM/data/5_13_2019/14_42/'

for file in os.listdir('data/5_13_2019/12_39'):

    flows = nwm_data.read_streamflow(path_1239+file, comids)['flows'][0]
    datetime = nwm_data.read_streamflow(path_1239+file, comids)['datetime']
    try:
        test.append(flows)
        print("flows{} working for file {}".format(flows, file))

    except:
        print("Error: flows NOT WORKING for file {}".format(flows, file))

    try:
        test2.append(datetime)
        print("datetime{} working for file {}".format(datetime, file))
    except:
        print("Error: datetime NOT WORKING for file {}".format(datetime, file))



for file in os.listdir('data/5_13_2019/13_40'):

    flows = nwm_data.read_streamflow(path_1340+file, comids)['flows'][0]
    datetime = nwm_data.read_streamflow(path_1340+file, comids)['datetime']
    try:
        test3.append(flows)
        print("flows{} working for file {}".format(flows, file))

    except:
        print("Error: flows NOT WORKING for file {}".format(flows, file))

    try:
        test4.append(datetime)
        print("datetime{} working for file {}".format(datetime, file))
    except:
        print("Error: datetime NOT WORKING for file {}".format(datetime, file))



for file in os.listdir('data/5_13_2019/14_42'):

    flows = nwm_data.read_streamflow(path_1442+file, comids)['flows'][0]
    datetime = nwm_data.read_streamflow(path_1442+file, comids)['datetime']
    try:
        test5.append(flows)
        print("flows{} working for file {}".format(flows, file))

    except:
        print("Error: flows NOT WORKING for file {}".format(flows, file))

    try:
        test6.append(datetime)
        print("datetime{} working for file {}".format(datetime, file))
    except:
        print("Error: datetime NOT WORKING for file {}".format(datetime, file))



#print(test)
print(test2)

test2= range(1,19)
testx= test2 + test4 + test6
testy= test + test3 + test5

plt.plot(testx,testy)
plt.show()



#print(file_list_1239)
# print("           ")
# print(file_list_1340)





