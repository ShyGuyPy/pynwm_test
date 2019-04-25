import netCDF4
import dateutil
import pytz
from bs4 import BeautifulSoup


#from pynwm import nwm_data
#import pynwm
#from pynwm.constants import PRODUCTSv1_1
#from pynwm import nwm_subset
import pynwm
from pynwm import nwm_data as nwm_data
from pynwm import nwm_subset as nwm_subset
#from nwm_data import read_streamflow as thing2
from pynwm.noaa import noaa_list as noaa_list
import csv
from netCDF4 import Dataset, num2date

#comids =[4507344, 4505568, 8450956, 4505878, 4505876, 4505912, 4505940, 4505944]
#comids =[4507344, 8450956, 4505878, 4505876, 4505940, 4505912, 4505944]
comids =[4505568]
netcdf_filename = "test.nc"
destination_file = "result.nc"

#result = pynwm.nwm_data.read_streamflow(netcdf_filename, comids)
result =  nwm_data.read_streamflow(netcdf_filename, comids)
#print(result)
nwm_subset.subset_channel_file(netcdf_filename, destination_file, comids)

nc = Dataset(destination_file, 'r', Format= 'NETCDF4')
#print(nc.variables)

print('Variable List')

for var in nc.variables:
    print(var)#, var.units, var.shape

reference_time_values =  nc.variables['reference_time'][:]
feature_id_values = nc.variables['feature_id'][:] 
time_values = nc.variables['time'][:]   
streamflow_values = nc.variables['streamflow'][:]
velocity_values = nc.variables['velocity'][:]

# print feature_id_values
# print time_values
# print streamflow_values
# print velocity_values


header = feature_id_values#['feature_id', 'streamflow', 'velocity']

with open('Output_test.csv', 'wb') as csvFile:
    outputwriter = csv.writer(csvFile, delimiter=',')
    outputwriter.writerow(header)
    #, time, streamflow, velocity
    #, time_values, streamflow_values, velocity_values
    #, time, streamflow, velocity

    #for feature_id, streamflow, velocity in zip(feature_id_values, streamflow_values, velocity_values):
    #    outputwriter.writerow( [feature_id, streamflow, velocity] )

    print("time:")
    for ref_time in zip(reference_time_values):
        for thing in ref_time:
            print(thing)
            #print thing
            #outputwriter.writerow( thing )

    print("test:")
    for test in zip(time_values):
        print(test)

    

csvFile.close()
nc.close()



#result2 =  thing.read_streamflow(destination_file, comids)
#print(result2)

#print('ID {0}: {1} cms at {2}'.format(comids[0], 
#                                      result['flows'][0],
#                                      result['datetime'][0]))

