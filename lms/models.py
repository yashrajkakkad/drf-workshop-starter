from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=30)
    intake = models.IntegerField()    
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    courses = models.ManyToManyField(Course, related_name="students")

    def __str__(self):
        return self.first_name + ' ' + self.last_name
