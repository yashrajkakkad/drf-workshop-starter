from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=30)

class Course(models.Model):
    name = models.CharField(max_length=30)
    intake = models.IntegerField()    
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    courses = models.ManyToManyField(Course, related_name="students")