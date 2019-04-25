import netCDF4
import dateutil
import pytz
from bs4 import BeautifulSoup

from pynwm import nwm_data, nwm_subset

comids =[4507344]
netcdf_filename = "test.nc"  # type: str
destination_file = "subset_result.nc"

#prints schema of the data
test =(nwm_data.get_schema(netCDF4.Dataset(netcdf_filename)))
test2 = nwm_data.read_streamflow(netcdf_filename, comids)
print(test2)
for i in test2:
        print i


#assign a variable to be output
#output = ""

#output the file 
# with open('Output_test.csv', 'wb') as csvFile:
#     outputwriter = csv.writer(csvFile, delimiter=',')
#     outputwriter.writerow(output)

