# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:09:26 2019

@author: Mico
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:57:26 2019

@author: Mico
"""

import pandas as pd
import os
import numpy as np

def enconde_string_category(df,df_clean,mapping,col_name):
    if col_name in class_mapping:
        categories = class_mapping[col_name]
        col_values = df[col_name].values
        encoded_values = []
        for value in col_values:
            encoded_value = categories.index(value.lower())
            encoded_values.append(encoded_value)
        print(encoded_values)
        df_clean[col_name] = encoded_values
        print(df_clean[col_name])
    else:
        column_data = pd.factorize(df[col_name].str.lower())
        mapping[col_name] = column_data[1].tolist()
        df_clean[col_name] = column_data[0]
    
    return df_clean, mapping

def column_to_float(df,col_name):
    col_list = []
    column_data = df[col_name]
    for row in column_data:
        col_list.append(float(str(row).replace(' in','').replace('.','.').replace('..','.')))
        
    return pd.DataFrame(col_list, columns=[col_name])
    
    
data_path = os.path.join('.','Datos_Entregable3_Hackathon.xlsx')
df = pd.read_excel(data_path,skiprows=2) #el header esta en la linea 

df = df.dropna() #quitamos las filas con datos NaN

headers = df.columns #nombres de los headers 

#constantes
altura_banco = 15 #15 metros
pasadura = 1 #1 metro
largo_pozo = altura_banco + pasadura

categorias = ['Fase','Tipo de tronadura','Tipo Material','M','Dominio Estructural','Tipo Explosivo']
floats = ['Banco','Diámetro','Fc','P10','P20','P30','P40','P50','P60','P70','P80','P90','P100','Este','Norte','Cota']
otros = ['BxS','Tiempo entre Pozos Filas ms']

clean_dataframe = pd.DataFrame()

# cargar mapping (numeros asignados a las variables categóricas)
class_mapping = np.load('mapping.npy').item()


#Fase
for header_name in headers:
    if header_name in categorias:
        clean_dataframe, class_mapping = enconde_string_category(df,clean_dataframe,class_mapping,header_name)
    else:
        if header_name in floats:
            clean_dataframe[header_name] = column_to_float(df,header_name)
            #clean_dataframe[header_name] = pd.to_numeric(df[header_name])               
             

                    
#otros

#BxS
if 'BxS' in headers:
    burden_list = []
    espaciamiento_list = []
    for bxs in df['BxS']:
        burden,espaciamiento = (bxs.lower()).split('x')
        burden_list.append(float(burden))
        espaciamiento_list.append(float(espaciamiento))
    
    clean_dataframe['Burden'] = burden_list
    clean_dataframe['Espaciamiento'] = espaciamiento_list      
    clean_dataframe['Area'] = clean_dataframe['Burden']*clean_dataframe['Espaciamiento']
    
if 'Tiempo entre Pozos Filas ms' in headers:    
    # tiempo entre pozos y filas ms
    tx_list = []
    ty_list = []
    
    for txy in df['Tiempo entre Pozos Filas ms']:
        tx,ty = txy.split('-')
        tx_list.append(float(tx))
        ty_list.append(float(ty))
        
    clean_dataframe['t_x'] = tx_list
    clean_dataframe['t_y'] = ty_list

clean_dataframe.to_excel('Datos_Entregable3_Hackathon_clean.xlsx', index = False)
#np.save('mapping.npy',class_mapping)


