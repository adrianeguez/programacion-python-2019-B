# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:40:51 2019

@author: USREPS
"""

# nombre = "Adrian"
# lista = [1,2,3]
import numpy as np
import pandas as pd

serie_num = pd.Series([1,2,3])

serie_varios = pd.Series(
        ["Adrian",
         2,
         True,
         None])

lista = [1,2,3]

print(type(serie_varios[3]))

serie_indices = pd.Series([
        "Adrian",
        "Vicente",
        "Carolina",
        "Wendy"], index=["A","V","C","W"])

print(serie_indices["A"])

valores_por_ciudad = {
        "Ibarra": 9500,
        "Guayaquil": 10000,
        "Cuenca": 7000,
        "Loja": 3000,
        "Quito": 8000
        }
serie_ciudades = pd.Series(
        valores_por_ciudad)

resp_menores = serie_ciudades < 6000

resp_filtro = serie_ciudades[resp_menores]












