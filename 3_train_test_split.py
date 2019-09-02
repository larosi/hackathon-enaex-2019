# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:30:29 2019

@author: laros
"""


import pandas as pd
import os
from sklearn.model_selection import train_test_split
import numpy as np


def softmax(x):
    smax = np.exp(x)/sum(np.exp(x))
    return smax

def inch2mm(x_inch):
    x_mm = 25.4000508001*x_inch
    return x_mm

# cargar dataset
data_filename = 'clean_database.xls'
data_path = os.path.join('.',data_filename)

df = pd.read_excel(data_path)

# ver los nombres de los datos
headers = df.columns
print(headers)

target_names = ['P10','P20','P30','P40','P50','P60','P70','P80','P90','P100']

target_data = pd.DataFrame()
#target_data['P0'] = 0*df['P10']
for target_name in target_names:
    target_data[target_name] = df[target_name]
    del df[target_name]
    
#eliminar datos redundantes
#del df['Banco']

# datos que no tiene coorelación con la fragmentación
#del df['Este']
#del df['Norte']


x = df
y = target_data
x_train, x_test, y_train, y_test = train_test_split(x.values, y.values, test_size=0.3, random_state=42)

np.save('train_test_data.npy',[x_train, x_test, y_train, y_test])

