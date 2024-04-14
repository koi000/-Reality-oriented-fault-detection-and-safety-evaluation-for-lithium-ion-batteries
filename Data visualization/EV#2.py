# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 15:26:45 2024

@author: admin
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%%
df = pd.read_csv('EV_2.csv')


cell_volt = df.filter(regex='单体电压')
cell_temp = df.filter(regex='探针温度')
warn = df['BMSWarningInformation']
pack_volt = df['BMSBatteryVoltage']
pack_SOC = df['vehBMSPackSOC']
time = df['time']
mile = df['vehOdo']

warn_loc_2 = np.where(warn==2)
x = np.arange(cell_volt.shape[1])/cell_volt.shape[1]
cm = plt.cm.get_cmap('Blues')
cm_s = plt.cm.get_cmap('viridis_r')
fig = plt.figure(figsize=(8,5), dpi=200)
for i in range(cell_volt.shape[1]):
    tmp = cell_volt.iloc[:,i]
    plt.plot(tmp, c=cm(x[i]), linewidth=2,alpha=0.8,linestyle='--')
    if i==82:
        plt.plot(tmp, color='#DC143C',linewidth=2, label='Faulty cell 83',alpha=0.8)
plt.axvline(warn_loc_2[0][1],color='#FF8C00',linewidth=4,alpha=0.6,linestyle='-.',label='BMS alarm')
plt.ylabel('Voltage (V)', fontsize=20)
plt.xlabel('Time (30s)', fontsize=20)
plt.yticks(fontsize=16)
plt.xticks(fontsize=16,rotation=20)

plt.show()

x = np.arange(cell_temp.shape[1])/cell_temp.shape[1]
cm = plt.cm.get_cmap('viridis_r')
cm_s = plt.cm.get_cmap('viridis_r')
fig = plt.figure(figsize=(8,5), dpi=200)
for i in range(cell_temp.shape[1]):
    tmp = cell_temp.iloc[:,i]
    plt.plot(tmp, c=cm(x[i]), linewidth=2,alpha=0.8,linestyle='--')
plt.axvline(warn_loc_2[0][1],color='#FF8C00',linewidth=4,alpha=0.6,linestyle='-.',label='BMS alarm')
plt.ylabel('Temperature (℃)', fontsize=20)
plt.xlabel('Time (30s)', fontsize=20)
plt.yticks(fontsize=16)
plt.xticks(fontsize=16,rotation=20)

plt.show()

