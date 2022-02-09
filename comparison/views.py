from django.shortcuts import render, redirect
from django.http import HttpResponse
from cargo.models import Contracts
import pandas as pd
from .functions import diff, difference, dataframe
# Create your views here.


#Vista para comparación de los 2 ultimos archivos
def comparison(request):
    #Traemos los 2 ultimos registros de la BD
    contracts = Contracts.objects.all().order_by('-id')[:2]   
    contract_1 = contracts[0]
    contract_2 = contracts[1]
    #Se leen los archivos para posteriormente convertirlos a dataframe para facilitar su manipulación
    xl = pd.ExcelFile(contract_1.file)
    xl2 = pd.ExcelFile(contract_2.file)
    sheets = xl.sheet_names
    df = xl.parse(sheets[0])
    df2 = xl2.parse(sheets[0])
    diffs = diff(df, df2)
    differences = difference(df, df2)
    #Se toma el dataframe mas grande como referencia a la hora de construir dataframe que se mostrara en el template
    #Las filas que no este presentes en 2do dataframe se toman como n.a.
    if len(df) > len(df2):
        df = dataframe(df, df2)  
    else:
        contract_1 = contracts[1]
        contract_2 = contracts[0]
        df = dataframe(df2, df)

    return render(request, "comparison/comparison.html", {'contract_1':contract_1, 'contract_2':contract_2, 'df':df, 'diffs':diffs, 'differences':differences})