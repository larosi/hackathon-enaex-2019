# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:30:29 2019

@author: laros
"""
import pandas as pd
import os
import random
import matplotlib.pyplot as plt
import numpy as np
# cargar dataset
data_filename = 'clean_database.xls'
data_path = os.path.join('.',data_filename)

df = pd.read_excel(data_path)

# ver los nombres de los datos
headers = df.columns
print(headers)

target_names = ['P10','P20','P30','P40','P50','P60','P70','P80','P90','P100']

target_data = pd.DataFrame()
target_data['P0'] = 0*df['P10']
for target_name in target_names:
    target_data[target_name] = df[target_name]
    del df[target_name]




i = random.randint(0,len(target_data))
sample = target_data.loc[i]

plt.plot(sample)
plt.show()

p_acc_x = np.arange(0,110,10)/100
p_acc_y = sample.values

plt.plot(p_acc_y,p_acc_x)
plt.show()


p_diff = np.gradient(p_acc_y,p_acc_x)

plt.plot(p_diff)
plt.show()

print(sum(p_diff))


