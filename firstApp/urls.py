from django.urls import path
from . import views

urlpatterns = [
    # goes to http://localhost:8000/firstApp/test_emp
    path('test_emp/', views.employeeDictView, name='emp_dict'),
    path('emps/', views.employeeDbView, name='emps_db'),
]
