# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 18:53:05 2019

@author: Mico
"""

from keras.models import load_model
import pandas as pd
import os

# cargar modelo entrenado
model = load_model('nn_model.h5')

# cargar datos de evaluacion
data_filename = 'Datos_Entregable2_Hackathon_clean.xlsx'
data_path = os.path.join('.',data_filename)
df = pd.read_excel(data_path)

x_eval = df.values

# predict y guardart
y_pred =  model.predict(x_eval)
predicted = pd.DataFrame(y_pred)

predicted.to_excel('Datos_Entregable2_Hackathon_predicted.xlsx', index = False)