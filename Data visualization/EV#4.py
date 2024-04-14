# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 16:15:43 2024

@author: admin
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick


#%%
df = pd.read_csv('EV_4.csv')

cell_volt = df.iloc[:,0:88]
cell_temp = df.iloc[:,88:120]
warn = df['BMSWarningInformation']
pack_volt = (df.iloc[:,121])
pack_SOC = (df.iloc[:,122])
time = (df.iloc[:,123])
mile = (df.iloc[:,124])


volt_tail = cell_volt.iloc[37150,:]/1000
overvoltage = np.where(volt_tail>4.2)[0]
undervoltage = np.where(volt_tail<3.6)[0]
nanvoltage = np.where(np.isnan(volt_tail))[0]
volt_fault = np.array(list(overvoltage) + list(undervoltage) + list(nanvoltage))

warn_loc_2 = np.where(warn==2)

x = np.arange(cell_volt.shape[1])/cell_volt.shape[1]
cm = plt.cm.get_cmap('Blues')
x_f = np.linspace(0.3,0.95,(len(overvoltage)+len(undervoltage)+len(nanvoltage)))
cm_f = plt.cm.get_cmap('Reds')
fig = plt.figure(figsize=(8,5), dpi=200) 
ax = fig.add_subplot(111)
for i in range(cell_volt.shape[1]):
    tmp = cell_volt.iloc[:,i]/1000
    plt.plot(tmp, c=cm(x[i]), linewidth=2,alpha=0.8,linestyle='-')
    if volt_tail[i]<3.6:
          plt.plot(tmp, linewidth=2, alpha=0.9,c=cm_f(x_f[np.where(volt_fault==i)[0]]))
    if volt_tail[i]>4.2:
          plt.plot(tmp, linewidth=2, alpha=0.9,c=cm_f(x_f[np.where(volt_fault==i)[0]]))
    if np.isnan(volt_tail[i]):
          plt.plot(tmp, linewidth=2, alpha=0.9,c=cm_f(x_f[np.where(volt_fault==i)[0]]))      

plt.axvline(warn_loc_2[0][0],color='#FF8C00',linewidth=4,alpha=0.6,linestyle='-.',label='BMS alarm')
plt.ylabel('Voltage (V)', fontsize=20)
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))
plt.xlabel('Time (30s)', fontsize=20)
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
plt.xlabel('Time (30s)', fontsize=20)
plt.yticks(fontsize=16)
plt.xticks(fontsize=16, rotation=20)
plt.show()
