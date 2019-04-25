import netCDF4
import dateutil
import pytz
from bs4 import BeautifulSoup

from pynwm import nwm_data, nwm_subset

comids = [4507344]

#the netcdf file to be used as a test
netcdf_filename = "test.nc"
#the destination of the subset data
destination_file = "result2.nc"
#subset the given netcdf data by the given comid and output
#the subset to the destination
nwm_subset.subset_channel_file(netcdf_filename,destination_file,comids)
#read the data back into a variable
my_data = netCDF4.Dataset(destination_file, 'r', Format= 'NETCDF4')
print(my_data)
