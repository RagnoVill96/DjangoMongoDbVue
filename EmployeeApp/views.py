from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

@csrf_exempt
def departmentApi(request, id = 0):
    if request.method == 'GET' :
        departments = Departments.objects.all()
        department_serializer = DepartmentSerializer(departments, many = True)
        return JsonResponse(department_serializer.data, safe=False)
    elif request.method == 'POST' :
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT' :
        Departments.objects.get(DepartmentId = 201)
        # department_data = JSONParser().parse(request)
        # print(department_data)
        # department = Departments.objects.get(DepartmentId = department_data['DepartmentId'])
        # print(department)
        # department_serializer = DepartmentSerializer(department, data = department_data)
        # if department_serializer.is_valid() :
        #    department_serializer.save()
        #    return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("put called", safe=False)
    elif request.method == 'DELETE' :
        print(Departments)
        department = Departments.objects.get(DepartmentId = id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    return JsonResponse("Deletion failed", safe=False)
# Create your views here.
