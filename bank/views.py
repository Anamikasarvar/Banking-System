from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import *

# Create your views here.

def home(request):
    return render(request,'bank/home.html')

def newcustomer(request):
    if request.method == "POST":
        fm = CustomerForm(request.POST)
        if fm.is_valid():
            # nm = request.POST['name']
            # num = request.POST['number']
            # em = request.POST['email']
            # blc = request.POST['balance']
            # form = Customer(name=nm,number=num,email=em,balance=blc)
            fm.save()
            messages.success(request, 'Your form has been submitted successfully!')
    return render(request, "bank/newcustomer.html")

def allcustomer(request):
    viewcustomer = Customer.objects.all()
    return render(request,'bank/allcustomer.html', {'customers':viewcustomer})

def customer_detail(request,pk):
    cm = Customer.objects.get(id = pk)
    ctm = Customer.objects.all()
    context = {"cm":cm,"ctm":ctm}

    if request.method == "POST":
        amount = request.POST.get('amount')
        receiver_name = request.POST.get('receiver_name')
        sender_name = cm.name
        customer_details = Transfer(sender_name=sender_name,amount=amount,receiver_name=receiver_name)
        customer_details.save()
        cm.delete()

        sender_balance = cm.balance - int(amount)
        sender_number = cm.number
        sender_email = cm.email
        # update_sender = Customer(name=sender_name,balance=sender_balance,number=sender_number,email=sender_email)
        update_sender = Customer(name=sender_name, number=sender_number, email=sender_email,
                                 balance=sender_balance)
        update_sender.save()

        receiver = Customer.objects.get(name=receiver_name)
        receiver_number = receiver.number
        receiver_email = receiver.email
        receiver_balance = receiver.balance + int(amount)
        receiver.delete()
        update_receiver = Customer(name=receiver_name, number=receiver_number, email= receiver_email,
                                   balance=receiver_balance)
        update_receiver.save()
        return redirect('/')

    return render(request,'bank/transfer.html',context)