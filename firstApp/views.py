from django.shortcuts import render
from django.http import JsonResponse

def employeeView(request):
    emp = {
        'id': 123,
        'name': 'John',
        'sal': 1000000
    }

    # JsonResponse is a Django serializer - it will retun the dictionary emp into JSON
    return JsonResponse(emp)