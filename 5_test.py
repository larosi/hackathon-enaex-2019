# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:33:03 2019

@author: Mico
"""

from keras.models import load_model
import numpy as np
import pandas as pd
from sklearn import metrics

# cargar modelo entrenado
model = load_model('nn_model.h5')

# cargar datos
x_train, x_test, y_train, y_test = np.load('train_test_data.npy')

y_pred =  model.predict(x_test)

y_diference = abs(y_test-y_pred)

target = pd.DataFrame(y_test)
predicted = pd.DataFrame(y_pred)
diference = pd.DataFrame(y_diference)

# Excel writter
writer = pd.ExcelWriter('prediction.xlsx', engine='xlsxwriter')

target.to_excel(writer, sheet_name='P_test')
predicted.to_excel(writer, sheet_name='P_predicted')
diference.to_excel(writer, sheet_name='P_diference')

test_MSE = metrics.mean_squared_error(y_test, y_pred, sample_weight=None, multioutput='uniform_average')
test_r2 =  metrics.r2_score(y_test, y_pred) 
test_MAE = metrics.mean_absolute_error(y_test, y_pred) 
print('test_MSE = {}'.format(test_MSE))
print('test_r2 = {}'.format(test_r2))
print('test_MAE = {}'.format(test_MAE))

writer.save()