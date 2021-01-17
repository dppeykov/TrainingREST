from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee

# ------ NOT USING THE DJANGO REST API FRAMEWORK, BUT JUST THE DJANGO WEB FRAMEWORK ---------------
# ------ Used just as an example how the web framework is handling such requests ------------------

def employeeDictView(request):
    emp = {
        'id': 123,
        'name': 'John',
        'sal': 1000000
    }

    # JsonResponse is a Django serializer - it will retun the dictionary emp into JSON
    return JsonResponse(emp)

def employeeDbView(request):

    data = Employee.objects.all()
    response = {'employees': list(data.values('name', 'sal'))}

    return JsonResponse(response)

# --------------------------------------------------------------------------------------------------