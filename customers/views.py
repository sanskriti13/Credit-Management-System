from django.shortcuts import render
from .models import Customer,Transaction


def home(request):
  return render(request,'customers/home.html')

def details(request,id):
  cust= Customer.objects.get(pk=id)
  return render(request,'customers/details.html',{'cust':cust})


def transaction(request,id):
  if request.method=="POST":
    s=Customer.objects.get(pk=id)
    recid= request.POST['receiver']
    amt=request.POST['amount']
    r=Customer.objects.get(pk=recid)
    r.balance+=int(amt)
    r.save()
    s.balance-=int(amt)
    s.save()
    
    t= Transaction.objects.create(send=s,rec=r,amount=amt)
    t.save()
    return render(request,'customers/success.html')
  cust= Customer.objects.all()
  return render(request,'customers/transaction.html',{'cust':cust,'id':id})

def dashboard(request):
  cust= Customer.objects.all()
  return render(request,'customers/dashboard.html',{'cust':cust})


def success(request):
  return render(request,'success.html')




# Create your views here.
