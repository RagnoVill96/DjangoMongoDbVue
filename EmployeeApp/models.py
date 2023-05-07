from django.db import models

# Create your models here.
class Departments(models.Model):
    DepartmentId = models.CharField(max_length=500)
    DepartmentName = models.CharField(max_length=500)

class Employees(models.Model):
    EmployeeId = models.CharField(max_length=500)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)