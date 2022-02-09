from django.shortcuts import render
from .forms import NewContract, FilterContract
from .models import Contracts, Rates
from .functions import excel
from django.db.models import Q

# Create your views here.
#Vista del formulario para la creación de contratos
def new_contract(request):
    form = NewContract()
    message = ''
    color = 'green'
    
    if request.method == 'POST':
        file_form = NewContract(request.POST, request.FILES)
        files = request.FILES.getlist('file') #field name in model
        
        for f in files:
            file = f
        data = request.POST
        if file_form.is_valid():
            data = request.POST
            contract = Contracts()
            contract.name = data['name']
            contract.date = data['date']
            contract.file = file
            contract.save()
            message = excel(contract.id, contract.file)
            #message = 'Se guardo correctamente'
            if message == 1:
                message = 'El contrato ha sido guardado correctamente.'
                color = 'green'
            else:
                color = 'red'
                #En caso de fallar el ingreso de los datos a la tabla Rates se elimina el contrato de la tabla Contract
                contract.delete()
                message = 'El archivo no pudo ser leído, asegúrese de que el formato y extensión sean los correctos o revise nuestro formato.'

    return render(request, "cargo/form.html", {'form': form, 'message': message, 'color':color})

#Vista el template que nos muestra todos los contratos registrados
def contracts(request):
    form = FilterContract()
    #filtra todos los contratos basado en los parametros que le enviamos desde el buscador, si no recibe nada regresa todos los contratos
    if request.method == 'GET': 
        data = request.GET
        if data:
            if data['name'] == '' and data['date'] == '':
                contracts = Contracts.objects.all()
            elif data['name'] != '' and data['date'] != '':
                contracts = Contracts.objects.filter(name = data['name'], date = data['date'])
            elif data['name'] == '':
                contracts = Contracts.objects.filter(date = data['date'])
            else:
                contracts = Contracts.objects.filter(name = data['name'])

        else:
            contracts = Contracts.objects.all()
    return render(request, "cargo/contracts.html", {'contracts': contracts, 'form':form})

#Una vez le clickeamos en el boton de ver en contracts nos muestra el contrato seleccionado junto a todas sus rutas registradas
def contract(request, contract_id):
    contract = Contracts.objects.get(id = contract_id)
    rates = Rates.objects.filter(contract = contract)
    return render(request, "cargo/contract.html", {'contract': contract, 'rates':rates})