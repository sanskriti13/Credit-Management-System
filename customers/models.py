from django.db import models
import uuid


class Customer(models.Model):
  custid= models.UUIDField(primary_key=True, default= uuid.uuid4,editable=False)
  img= models.ImageField(upload_to="photos/customers", blank=True)
  name= models.CharField(max_length= 100)
  email= models.EmailField(unique=True)
  balance= models.FloatField(default=1000.00)

  def __str__(self):
    return self.name


class Transaction(models.Model):
  tid= models.AutoField(primary_key=True)
  rec = models.CharField(max_length=70,blank=True)
  send = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True, related_name= 'send')
  rec = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True, related_name= 'rec')
  amount= models.FloatField()

