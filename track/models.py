from django.db import models
import datetime

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200, null=True,blank=True)
    email = models.CharField(max_length=200, blank=True,null=True)
    designation = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name


class Asset(models.Model):
    Devise = [
        ('PHONE','Phone'),
        ('TABLET','Tablet'),
        ('LAPTOP','Laptop')
    ]
    
    asset_type = models.CharField(max_length=200,choices=Devise)
    model_no = models.CharField(max_length=200)
    brand = models.CharField(max_length=200,null=True,blank=True)
    


    def __str__(self):
        return self.model_no



class DelegateTo(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='delegateto')
    assets = models.ManyToManyField(Asset,null=True,blank=True,related_name='asset')
    checked_out_at = models.DateTimeField(default=datetime.datetime.now)
    condition = models.CharField(max_length=200,null=True,blank=True)
    

    def __str__(self):
        return str(self.employee)



class GiveBack(models.Model):
    returned_condition = models.CharField(max_length=200)
    returned_date = models.DateTimeField(default=datetime.datetime.now)
    delegat = models.ForeignKey(DelegateTo,on_delete=models.CASCADE,related_name='employee_name')
    model = models.ForeignKey(Asset,on_delete=models.CASCADE,related_name='asset_model')

    @property
    def checked_out_time(self):
        return self.delegat.checked_out_at

    @property
    def asset_type(self):
        return self.model.asset_type

    @property
    def delegate_condition(self):
        return self.delegat.condition
    @property
    def employee_name(self):
        return self.delegat.employee.name
    
    @property
    def brand(self):
        return self.model.brand
