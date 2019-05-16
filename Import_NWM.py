import os

from pynwm import nwm_data

import matplotlib.pyplot as plt

comids =[4507344]
plot_y = []
plot_x = []

path_t_23z = 'C:/Users/icprbadmin/Documents/Python_Scripts/NWM/data/5_15_2019/t_23z/'

for file in os.listdir('data/5_15_2019/t_23z'):

    flows = nwm_data.read_streamflow(path_t_23z+file, comids)['flows'][0]
    datetime = nwm_data.read_streamflow(path_t_23z+file, comids)['datetime']
    try:
        plot_y.append(flows)
        print("flows{} working for file {}".format(flows, file))

    except:
        print("Error: flows NOT WORKING for file {}".format(flows, file))

    try:
        plot_x.append(datetime)
        print("datetime{} working for file {}".format(datetime, file))
    except:
        print("Error: datetime NOT WORKING for file {}".format(datetime, file))


plt.plot(plot_x,plot_y)
plt.show()