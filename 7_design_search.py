# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:17:26 2019

@author: laros
"""

import pandas as pd
import os

from keras.models import load_model


# cargar modelo entrenado
model = load_model('nn_model.h5')

summary = model.summary()
W_Input_Hidden = model.layers[0].get_weights()[0]

print(summary)
print(W_Input_Hidden)
file_path = os.path.join('.','Datos_Entregable3_Hackathon.xlsx')
df = pd.read_excel(file_path,skiprows=2)

param_design = ['Diámetro','Fc','Tipo Explosivo','Burden','Espaciamiento','t_x','t_y']

