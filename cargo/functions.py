import pandas as pd
from .models import Rates, Contracts


#función para guardar los datos del excel en la tabla Rates

def excel(contract_id, file):
    xl = pd.ExcelFile(file)
    sheets = xl.sheet_names
    df = xl.parse(sheets[0])
    try:
        #Se definen las columnas que iran a la BD
        df2 = df[["POL","POD","Curr.","20'GP","40'GP","40'HC"]]
        contract = Contracts.objects.get(id = contract_id)
        #Se recorre el dataframe y se guarda en BD
        for i in range(len(df2)): 
            rates = Rates()
            rates.pol = df.loc[i,"POL"]
            rates.pod = df.loc[i,"POD"]
            rates.curr = df.loc[i,"Curr."]
            rates.twenty = df.loc[i,"20'GP"]
            rates.forty = df.loc[i,"40'GP"]
            rates.fortyhc = df.loc[i,"40'HC"]
            rates.contract = contract
            rates.save()
    except:
        #En caso de fallar regresa un 0 que nos indica fallo, si tiene éxito regresa 1
        return 0
    return 1
