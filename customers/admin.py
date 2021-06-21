from django.contrib import admin
from .models import Customer,Transaction

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
  list_display=['custid', 'name', 'balance', 'email']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
  list_display=['tid', 'rec', 'send', 'amount']
