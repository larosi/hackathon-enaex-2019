# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:17:26 2019

@author: laros
"""

import pandas as pd
import os

from keras.models import load_model
import numpy as np
import random

# constantes
inch_meter = 0.0254
altura_banco = 15 #15 metros
pasadura = 1 #1 metro
largo_pozo = altura_banco + pasadura


# cargar modelo entrenado
model = load_model('nn_model.h5')


file_path = os.path.join('.','Datos_Entregable3_Hackathon_clean.xlsx')
df = pd.read_excel(file_path)

p_values_expected = (df.iloc[:, 6:16]).values
p_values_names = ['P10','P20','P30','P40','P50','P60','P70','P80','P90','P100']
params_mina = df.copy()
for p_name in p_values_names:
    del params_mina[p_name]
    
#df2 = datasX.iloc[:, 72:]

# cargar los datos historicos (excel 1)
dataset_features, p_values = np.load('dataset.npy')
# cargar mapping (numeros asignados a las variables categóricas)
class_mapping = np.load('mapping.npy').item()

p_values.loc()
writer = pd.ExcelWriter('factible_designs.xlsx', engine='xlsxwriter')
for dfactible_i in range(0,params_mina.shape[0]):
    p_query = p_values_expected[dfactible_i]
    param_mina = params_mina.loc[dfactible_i]
    
    param_filters = ['Cota','Fase','Tipo de tronadura','Tipo Material','M','Dominio Estructural']
    filter_list = []
    for param_filter in param_filters:
        filter_mask = dataset_features[param_filter] == param_mina[param_filter]
        filter_list.append(filter_mask)
    
    condition = filter_list.pop()
    for cond in filter_list:
        new_condition = condition & cond
        if(new_condition.max()):
            condition = new_condition
    
    
    p_values_filtered = p_values[condition]
    
    l2_dist = np.sqrt(((p_values_filtered - p_query)**2).sum(axis=1))
    
    l2_dist_sorted = l2_dist.sort_values()
    
    nearest_index = l2_dist_sorted.index[0]
    
    print(p_values_filtered.loc[nearest_index])
    print(dataset_features.loc[nearest_index])
    
    design_space_header = dataset_features.columns
    param_mina_header = params_mina.columns
    design_space = []

    # parametros a buscar
    diametros = [12.25,11,10,8,6.5,6]
    t_explosivos = [0,1,2,3,4,5,6,7,8,9]
    fc_mean = dataset_features.loc[nearest_index]['Fc']
    for iteration in range(0,50):
        for diametro in diametros:
            for explosivo in t_explosivos:
                current_param = {}
                current_param['Diámetro'] = diametro
                current_param['Tipo Explosivo'] = explosivo
                
                fc = fc_mean+random.randint( max(-250,100-fc_mean),min(250,800-fc_mean))
                #fc = random.randint(100,1000)
                current_param['Fc'] = fc
            
                area = random.randint(31,225)#burden*espaciamiento
                ratio = random.randint(10,40)/20
                espaciamiento = int(np.sqrt(area/ratio))
                burden = int(area/espaciamiento)
                area = espaciamiento*burden
                current_param['Area'] = area
                current_param['Burden'] = burden
                current_param['Espaciamiento'] = espaciamiento
                
                #print('BxS {}  = B {} x S {}'.format(area,burden,espaciamiento))
                t_x = min(max(dataset_features.loc[nearest_index]['t_x']+random.randint(-3,3),1),200)
                t_y = min(max(dataset_features.loc[nearest_index]['t_y']+random.randint(-20,20),1),2000)
                current_param['t_x'] = t_x
                current_param['t_y'] = t_y
                feature_vector = []
                for header_name in design_space_header:
                    if header_name in param_mina_header:
                        feature_vector.append(param_mina[header_name])
                    else:
                        feature_vector.append(current_param[header_name])
                
                design_space.append(feature_vector)
    df_design_space = pd.DataFrame(design_space, columns=design_space_header)
    y_pred =  model.predict(df_design_space)
    predicted_p = pd.DataFrame(y_pred,columns=p_values_names)
    
    l2_dist_predicted = np.sqrt(((predicted_p - p_query)**2).sum(axis=1))

    l2_dist_predicted_sorted = l2_dist_predicted.sort_values()
    factible_bool = l2_dist_predicted_sorted<max(1.3,l2_dist_predicted_sorted.min()*1.2) #la distancia es menor a un margen
    p_predicted_factible = pd.DataFrame(predicted_p[factible_bool].values, columns=predicted_p.columns)
    factible_design = pd.DataFrame(df_design_space[factible_bool].values, columns=df_design_space.columns)
    df_l2_distance = pd.DataFrame(l2_dist_predicted_sorted[0:len(p_predicted_factible)].values, columns=['l2 distance'])
    
    factible_result = pd.concat([factible_design,p_predicted_factible,df_l2_distance], axis=1)
    #factible_result.rename(columns={0:'l2 dist'}, inplace=True)
    
    # guadar diseños factibles, un sheet para cada diseño pedido
    design_name = 'dfactible_{}'.format(dfactible_i+2)
    factible_result.to_excel(writer, sheet_name=design_name,index=False)
writer.save()

print('listo!')
    