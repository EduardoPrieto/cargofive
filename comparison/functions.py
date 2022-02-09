import pandas as pd
import json

#Encuentra las diferencias entre las diferentes filas de los archivos
def diff(df, df2):
    #Regresa un False si hay algun dato diferente en la fila
    diff = df.eq(df2).all(axis=1)
    diff_t = 0
    diff_f = 0
    for i in range(len(diff)):
        if diff.loc[i] == True:
            diff_t += 1
        else:
            diff_f += 1
    return {'diff_t':diff_t, 'diff_f':diff_f}

#Encuentra las diferencias entre los diferentes datos de los archivos
def difference(df, df2):
    #Regresa false a los datos diferentes y true a los datos iguales
    difference = df.eq(df2)
    #Cambia los nombres de las columnas por numeros facilitar la iteración
    x = range(len(difference.columns))
    difference.columns = x
    difference.columns
    difference_t = difference_f = 0
    for i in range(len(difference)):
        for j in range(len(difference.columns)):
            if difference.loc[i][j] == True:
                difference_t += 1
            else:
                difference_f += 1
    return {'difference_t':difference_t, 'difference_f':difference_f}

#Genera un dataframe con la combinación de los datos suministrados por el cliente
def dataframe(df, df2):
    x = range(len(df.columns))
    columns = df.columns
    for i in range(len(df)):
        for j in range(len(df.columns)):
            try:
                if df.loc[i][columns[j]] != df2.loc[i][columns[j]]:
                    df.loc[i][columns[j]] = str(df.loc[i][columns[j]]) + ' - ' + str(df2.loc[i][columns[j]])
            except:
                if df.loc[i][columns[j]]:
                    df.loc[i][columns[j]] = str(df.loc[i][columns[j]]) + ' - n.a.' 
    columns_2 = split_list(columns)
    df.columns = columns_2
    #Convertimos el dataframe en un archivo json para facilitar la manipulación en el template
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return context

#Para facilitar el manejo de los datos se retiran las comillas y los puntos de los nombres de las columnas
def split_list(columns):
    columns_2 = []
    for item in columns:
        list = item.split(".")
        if len(list) == 2:
            item = str(list[0]) + '' + str(list[1])
        else:
            item = str(list[0])
        list = item.split("'")
        if len(list) == 2:
            item = str(list[0]) + '' + str(list[1])
        else:
            item = str(list[0])
        columns_2.append(item)

    return columns_2


