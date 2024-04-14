# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 15:58:14 2024

@author: admin
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%%
df = pd.read_csv('EV_3.csv')

cell_volt = df.filter(regex='单体电压')
cell_temp = df.filter(regex='探针温度')
warn = df['BMSWarningInformation']
pack_volt = df['BMSBatteryVoltage']
pack_SOC = df['vehBMSPackSOC']
time = df['time']
mile = df['vehOdo']


warn_loc_2 = np.where(warn==2)
volt_tail = cell_volt.iloc[-1,:]/1000
x = np.arange(cell_volt.shape[1])/cell_volt.shape[1]
cm = plt.cm.get_cmap('Blues')
x_f = np.linspace(0.5,0.9,len(np.where(volt_tail<3.5)[0]))
cm_f = plt.cm.get_cmap('Reds')
fig = plt.figure(figsize=(8,5), dpi=200)
for i in range(cell_volt.shape[1]):
    tmp = cell_volt.iloc[:,i]/1000
    plt.plot(tmp, c=cm(x[i]), linewidth=2,alpha=0.8,linestyle='-')
    if volt_tail[i]<3.5:
          plt.plot(tmp, linewidth=2, alpha=0.9,c=cm_f(x_f[i-73]))

plt.axvline(warn_loc_2[0][0],color='#FF8C00',linewidth=4,alpha=0.6,linestyle='-.',label='BMS alarm')

plt.ylabel('Voltage (V)', fontsize=20)
plt.xlabel('Time (10s)', fontsize=20)
plt.yticks(fontsize=16)
plt.xticks(fontsize=16, rotation=20)
plt.show()




x_t = np.arange(cell_temp.shape[1])/cell_temp.shape[1]
cm_t = plt.cm.get_cmap('viridis_r')

fig = plt.figure(figsize=(8,5), dpi=200)
for i in range(cell_temp.shape[1]):
    tmp = cell_temp.iloc[:,i]
    plt.plot(tmp, c=cm_t(x_t[i]), linewidth=2,alpha=0.8,linestyle='-')

plt.axvline(warn_loc_2[0][0],color='#FF8C00',linewidth=4,alpha=0.6,linestyle='-.',label='BMS alarm')
plt.ylabel('Temperature (℃)', fontsize=20)
plt.xlabel('Time (10s)', fontsize=20)
plt.yticks(fontsize=16)
plt.xticks(fontsize=16, rotation=20)
plt.show()

#%%
