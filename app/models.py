from django.db import models

# Create your models here.
class School(models.Model):
    sname=models.CharField(max_length=100,primary_key=True)
    sprincipal=models.CharField(max_length=100)
    def __str__(self):
        return self.sname
class Student(models.Model):
    sname=models.ForeignKey(School,on_delete=models.CASCADE)
    std_name=models.CharField(max_length=100)
    cls=models.BigIntegerField()
    email=models.URLField()
    def __str__(self):
        return self.std_name