# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:30:29 2019

@author: laros
"""


import pandas as pd
import os
from sklearn.model_selection import train_test_split
import numpy as np

p_predictor = False
# cargar dataset
data_filename = 'clean_database.xls'
data_path = os.path.join('.',data_filename)

df = pd.read_excel(data_path)

# ver los nombres de los datos
headers = df.columns
print(headers)

if(p_predictor):
    target_names = ['P10','P20','P30','P40','P50','P60','P70','P80','P90','P100']
    remove_names = []
else:
    target_names = ['Fc']
    #target_names = ['Fc', 'Burden', 'Espaciamiento','Area','t_x','t_y']
    remove_names = ['Diámetro','Area','Burden', 'Espaciamiento','t_x','t_y']

target_data = pd.DataFrame()
#target_data['P0'] = 0*df['P10']
for target_name in target_names:
    target_data[target_name] = df[target_name]
    del df[target_name]

for name_to_remove in remove_names:
    del df[name_to_remove]
    
#eliminar datos redundantes
#del df['Banco']

# datos que no tiene coorelación con la fragmentación
#del df['Este']
#del df['Norte']


x = df
y = target_data
print('features:')
print(x.columns)
print('')
print('target')
print(y.columns)

x_train, x_test, y_train, y_test = train_test_split(x.values, y.values, test_size=0.3, random_state=42)

if(p_predictor):
    np.save('train_test_data.npy',[x_train, x_test, y_train, y_test])
else:
    np.save('train_test_data2.npy',[x_train, x_test, y_train, y_test])

