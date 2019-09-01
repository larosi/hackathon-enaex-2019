# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:16:55 2019

@author: laros
"""


import pandas as pd
import os

# cargar dataset
data_filename = 'clean_database.xls'
data_path = os.path.join('.',data_filename)

df = pd.read_excel(data_path)

# ver los nombres de los datos
headers = df.columns
print(headers)
   

#correlación 
correlation_matrix = df.corr()

correlation_matrix.round(2).to_excel('correlation_matrix.xls')
