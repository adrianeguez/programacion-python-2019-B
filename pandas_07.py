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

CSV_PATH = "./titanic.csv"
df = pd.read_csv(CSV_PATH, 
                 nrows=5, 
                 index_col = 'PassengerId',
                 usecols = ['PassengerId','Survived','Name'])


# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 07:57:30 2019
@author: USRBET
"""
import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

serie_a = pd.Series(
        lista_numeros)
serie_b = pd.Series(
        tupla_numeros)
serie_c = pd.Series(
        np_numeros)
serie_d = pd.Series([
        True,
        False,
        12,
        12.12,
        "1",
        None,
        (),
        [],
        {"nombre":"Adrian"}])

serie_d[3]

lista_ciudades = ["Ambato",
                  "Cuenca",
                  "Loja",
                  "Quito"]

serie_ciudad = pd.Series(
        lista_ciudades,
        index=[
                "A",
                "C",
                "L",
                "Q",
                ])

serie_ciudad["Q"]
serie_ciudad[3]

valores_ciudad = {
        "Ibarra": 9500,
        "Guayaquil": 10000,
        "Cuenca": 7000,
        "Quito":8000,
        "Loja":3000
        }
serie_valor_ciudad = pd.Series(
        valores_ciudad)
serie_valor_ciudad[0]
serie_valor_ciudad["Ibarra"]

ciudades_menores_5000 = serie_valor_ciudad < 5000


s5 = serie_valor_ciudad[ciudades_menores_5000]

serie_valor_ciudad = serie_valor_ciudad * 1.1

serie_valor_ciudad["Quito"] = serie_valor_ciudad["Quito"] - 50

print("Lima" in serie_valor_ciudad)
print("Loja" in serie_valor_ciudad)

rsquare = np.square(serie_valor_ciudad)

ciudades_uno = pd.Series({
        "Montañita":300,
        "Guayaquil":10000,
        "Quito":2000})

ciudades_dos = pd.Series({
        "Loja":300,
        "Guayaquil":10000})

ciudades_uno["Loja"] = 0

print(ciudades_uno + ciudades_dos)

ciu_add = ciudades_uno.add(ciudades_dos)

ciu_concatenadas = pd.concat([
        ciudades_uno,
        ciudades_dos])

ciu_concatenadas_v = pd.concat([
        ciudades_uno,
        ciudades_dos
        ], verify_integrity = True)

## Concat y Append son lo mismo

ciu_append = ciudades_uno.append(
        ciudades_dos,
        verify_integrity = True)

ciudades_uno.max()
pd.Series.max(ciudades_uno)
np.max(ciudades_uno)

ciudades_uno.min()
pd.Series.min(ciudades_uno)
np.min(ciudades_uno)

# Estadistica
ciudades_uno.mean()
ciudades_uno.median()
np.average(ciudades_uno)

ciudades_uno.head(2)
ciudades_uno.tail(2)

ciudades_uno.sort_values(
        ascending = False).head(2)
ciudades_uno.sort_values().tail(2)

# 0 - 1000 5%
# 1001 - 5000 10%
# 5001 - 20000 15%

def calculo(valor):
    if(valor <= 1000):
        return valor * 1.05
    if(valor > 1000 and valor <= 5000):
        return valor * 1.10
    if(valor > 5000):
        return valor * 1.15

ciudad_calculada = ciudades_uno.map(calculo)

# Cuando NO CUMPLE la condicion
# Aplica la formula
ciudades_uno.where(ciudades_uno < 1000, 
                   ciudades_uno * 1.05)


import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)

df1 = pd.DataFrame(arr_pand)
s1 = df1[0]
s2 = df1[1]
s3 = df1[2]
s1[0]

df1[3] = s1

df1[4] = s1 * s2

datos_fisicos_uno = pd.DataFrame(
        arr_pand,
        columns=[
                'Estatura (cm)',
                'Peso (kg)',
                'edad(anios)'])

datos_fisicos_dos = pd.DataFrame(
        arr_pand,
        columns=[
                'Estatura (cm)',
                'Peso (kg)',
                'edad(anios)'],
        index=['Adrian','Vicente'])

df1.index = ['Adrian', 'Vicente']
df1.index = ['Pepe', 'Vicente']
df1.columns = ['A','B','C','D','F']





import pandas as pd

path_guardado_bin = "C://Users//USRBET//Documents//GitHub//py-eguez-sarzosa-vicente-adrian//03 - pandas//data//artwork_data_completo.pickle"

df = pd.read_pickle(path_guardado_bin)

## Obtener nombres de los artistas

serie_artistas_repetidos = df["artist"]

artistas = pd.unique(serie_artistas_repetidos)

artistas.size
len(artistas)

blake = df["artist"] == "Blake, William"

blake.value_counts()
df["artist"].value_counts()

df_blake = df[blake]



import pandas as pd

path_guardado_bin = "C://Users//USRBET//Documents//GitHub//py-eguez-sarzosa-vicente-adrian//03 - pandas//data//artwork_data_completo.pickle"

df = pd.read_pickle(path_guardado_bin)
df2 = df.set_index('id')
"""
NOMBRE         nota 1    disciplina
Pepito        7           5
Juanita       8           9
Maria         9           2
"""
datos = {
        "nota 1":{
                "Pepito":7,
                "Juanita":8,
                "Maria":9},
        "disciplina":{
                "Pepito":5,
                "Juanita":9,
                "Maria":2}
        }
notas = pd.DataFrame(datos)
notas.loc["Pepito"]
notas.iloc[0]
type(notas.loc["Pepito"]) # Serie

notas.loc["Pepito","disciplina"]

notas.loc["Pepito",["disciplina","nota 1"]]

notas.loc[["Pepito","Juanita"], ["nota 1"]]

notas.loc[["Pepito","Juanita"], "nota 1"]

notas.loc[[True, False, True]]

condicion_nota = notas["nota 1"] > 7
condicion_disc = notas["disciplina"] > 7

mayores_siete = notas.loc[ condicion_nota, ["nota 1"] ]

mayores_siete = notas.loc[condicion_nota][condicion_disc]

## notas.loc[condicion_nota]
## mayores_siete[condicion_disc]


notas.loc["Maria","disciplina"] = 7

# Estudiantes menores a 7 en disciplina
# Suben a 7

# Solo a pepito se le va a poner 10 en todo

# Disciplina se les baje a 7

notas.loc[:,"disciplina"] = 7

# Anadir la columna promedio nota 1 y disciplina



primero = df2.loc[0]

primero = df2.iloc[0]








