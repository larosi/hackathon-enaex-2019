# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 20:51:32 2019

@author: Mico
"""

import pandas as pd

xls = pd.ExcelFile('factible_designs.xlsx')

n_sheets = 10
lista_sol_optimas = []
for sheet_i in range(0,n_sheets):
    sheet_name='dfactible_{}'.format(sheet_i+1)
    df = pd.read_excel(xls,sheet_name)
    
    lista_costos = []
    for row_i in range(0,df.shape[0]):
        m = int(df['M'][row_i])
        diametro = df['Diámetro'][row_i]
        area = df['Area'][row_i]
        fc = df['Fc'][row_i]
        t_explosivo = df['Tipo Explosivo'][row_i]
        
        # constantes
        inch_meter = 0.0254
        altura_banco = 15 #15 metros
        pasadura = 1 #1 metro
        largo_pozo = altura_banco + pasadura
        
        costos_explosivos = [1284,1266,2727,2727,2247,1878,1878,2264,2229,1302] #dolares/tonelada
        rho_explosivos = [1.32,1.32,1.32,1.32,1.3,1.34,1.32,1.32,1,1] #gr/ml = ton/m3
        
        diametros = [12.25,11.0,10.0,8.0,6.5,6.0]
        costos_perforacion = [42,48,57,66,78,81]
        rho_roca = [2.65,2.74,2.53,2.65,2.65,2.53]
        
        rho_m = rho_roca[m]     
        ton_roca = area*altura_banco*rho_m
        gr_explosivo = fc*ton_roca
        
        #costos diseño actual

        costo_perforacion = costos_perforacion[diametros.index(diametro)] #dolares/metro
        costo_explosivo = costos_explosivos[t_explosivo] #dolares/tonelada
        
        
        costo_total_explosivo = fc*costo_explosivo/10e6
        costo_total_perforacion = costo_perforacion * largo_pozo / ton_roca
        
        costo_tronadura = costo_total_perforacion + costo_total_explosivo #dolares/tonelada
        lista_costos.append(costo_tronadura)
    costo_min = min(lista_costos)
    index_min = lista_costos.index(costo_min)
    print(sheet_name)
    print(costo_min)
    print(index_min)
    tronadura_costo_min = df.iloc[index_min,:]
    print(tronadura_costo_min)
    lista_sol_optimas.append(tronadura_costo_min)
