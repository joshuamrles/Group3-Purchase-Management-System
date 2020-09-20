from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.template import RequestContext
from django.db import models
from datetime import datetime
from app.models import Person,Item,Vendor
from RequestOfQuotation.models import RequestOfQuotation,RequestOfQuotationItem
from PurchaseRequisition.models import PurchaseRequisition,PurchaseRequisitionItem
from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from django.http.request import QueryDict
from decimal import Decimal
from prettytable import PrettyTable
from django.core.mail import send_mail
from django.conf import settings
import random
import datetime 

@login_required
def requestofquotationform(request):
    context = {
            'title':'Request Of Quotation Form'
        }
    context['user'] = request.user

    return render(request,'RequestOfQuotation/requestofquotationform.html',context)

@login_required

def fillingrequestofquotation(request):

    context = {}
    pr_id = request.GET['pr_id']

    roq_id = 1001

    roq = RequestOfQuotation.objects.all()
    numberroq = len(roq)
    roq_id = int(roq_id) + int(numberroq) 

    staff_id = request.user.id
    staff_info = Person.objects.get(user_id = staff_id)

    try: 
       
        purchase_requisition = PurchaseRequisition.objects.get(pr_id = pr_id)
        item_list = PurchaseRequisitionItem.objects.filter(pr_id = pr_id)
        context = {
                'title': 'Request Of Quotation Form',
                'request_of_quotation_id': 'ROQ' + str(roq_id),
                'purchase_requisition_id': pr_id, 
                'staff_id' : staff_info.person_id,
                'rows':item_list
            }

        return render(request,'RequestOfQuotation/requestofquotationform.html',context)

    except PurchaseRequisition.DoesNotExist:

        context = { 'error': 'The Purchase Requisition id is invalid !',
                    'title': 'Request Of Quotation Form'
            }
        return render(request,'RequestOfQuotation/requestofquotationform.html',context)

def requestofquotationconfirmation(request):

    context = {}
    roq_id = request.POST['request_of_quotation_id']
    purchase_requisition_id = request.POST['purchase_requisition_id']
    staff_id = request.user.id
    vendor_id = request.POST['vendor_id']
    description = request.POST['description']
    staff_info = Person.objects.get(user_id = staff_id)
    responses = request.read()
    print(responses)
   
    q= QueryDict(responses)
    
    items_id = q.getlist('item_id')
    print(items_id)
    items_name = q.getlist('item_name')
    print(items_name)
    items_quantity = q.getlist('quantity')
    print(items_quantity)
    items_unit_price = q.getlist('unit_price')
    print(items_unit_price)
    items_total_price = q.getlist('total_price')
    print(items_total_price)


    items = list()

    i = 0
    items_length = len(items_id)
    grand_total = Decimal(0)

    while i < items_length:
        total= Decimal(items_quantity[i]) * Decimal(items_unit_price[i])
        item_table = {
            'item_name':items_name[i],
            'item_id': items_id[i],
            'quantity' : items_quantity[i],
            'unit_price': items_unit_price[i],
            'total_price': total
        }
        items.append(item_table)
        i = i + 1
        grand_total = grand_total + total
    print(items)

    try:
        vendor_info = Vendor.objects.get(vendor_id = vendor_id)


        context = {
                'title': 'Request Of Quotation Confirmation',
                'purchase_requisition_id' : purchase_requisition_id,
                'request_of_quotation_id' : roq_id,
                'staff_id' : staff_id,
                'vendor_id' : vendor_id,
                'grand_total': grand_total,
                'rows' : items,
                'staff_info' : staff_info,
                'vendor_info' : vendor_info,
                'description' : description
            }


        return render(request,'RequestOfQuotation/requestofquotationconfirmation.html',context)
    except Vendor.DoesNotExist:


        context = { 'error': 'Please insert valid vendor ID!',
                    'title': 'Request Of Quotation Form',
            }
        return render(request,'RequestOfQuotation/requestofquotationform.html',context)

 
def requestofquotationdetails(request):
    context = {}
    roq_id = request.POST['request_of_quotation_id']
    purchase_requisition_id = request.POST['purchase_requisition_id']
    staff_id = request.user.id
    vendor_id = request.POST['vendor_id']
    description = request.POST['description']
    purchase_requisition = PurchaseRequisition.objects.get(pr_id = purchase_requisition_id)
    staff_info = Person.objects.get(user_id = staff_id)
    vendor_info = Vendor.objects.get(vendor_id = vendor_id)

    responses = request.read()
    print(responses)
   
    q= QueryDict(responses)
    
    items_id = q.getlist('item_id')
    print(items_id)
    items_name = q.getlist('item_name')
    print(items_name)
    items_quantity = q.getlist('quantity')
    print(items_quantity)
    items_unit_price = q.getlist('unit_price')
    print(items_unit_price)
    items_total_price = q.getlist('total_price')
    print(items_total_price)


    items = list()

    i = 0
    items_length = len(items_id)
    grand_total = Decimal(0)

    while i < items_length:
        total= Decimal(items_quantity[i]) * Decimal(items_unit_price[i])
        item_table = {
            'item_name': items_name[i],
            'item_id': items_id[i],
            'quantity' : items_quantity[i],
            'unit_price': items_unit_price[i],
            'total_price': total
        }
        items.append(item_table)
        i = i + 1
        grand_total = grand_total + total
    print(items)

 

    # push the data to the database 
    current_time = datetime.datetime.now() 
    print(current_time)
    roq_info = RequestOfQuotation(request_of_quotation_id = roq_id, 
                            time_created = current_time,
                            total_price = grand_total, 
                            person_id = staff_info,
                            description = description,
                            vendor_id = vendor_info, 
                            purchase_requisition_id = purchase_requisition)
    roq_info.save()

    request_of_quotation = RequestOfQuotation.objects.get(request_of_quotation_id = roq_id)
    for item in items:
        item_info = Item.objects.get(item_id = item['item_id'])
        roq_item_info = RequestOfQuotationItem(request_of_quotation_id = request_of_quotation, 
                                         item_id = item_info, 
                                         quantity = item['quantity'], 
                                         unit_price = item['unit_price'],
                                         total_price = item['total_price'])
        roq_item_info.save()

    # update status purchase requisition
    pr = PurchaseRequisition.objects.get(pr_id = purchase_requisition_id)
    pr.status = 'APPROVED'
    pr.save()

    print(pr)

    #send email to vendor
    x = PrettyTable()

    x.field_names = ["Item ID","Item Name","Quantity","Unit Price","Total Price"]

    for item in items:
        x.add_row([item['item_id'],item['item_name'],item['quantity'],item['unit_price'],item['total_price']])

    subject = 'REQUEST OF QUOTATION INFORMATION: '+ roq_id
    message = 'This is the Request of Quotation Order Information: \n'+'Person In Charge: '+staff_info.person_name+'\n'+staff_info.person_address+ '\n' +'Request of Quotation Number: ' + roq_id + '\n'+ '\n'+'Time Issued: ' + str(current_time) + '\n'+'Vendor ID: ' + vendor_id + '\n'+'Description: ' + description + '\n'+ str(x) +'\n'

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [vendor_info.vendor_email,]
    send_mail( subject, message, email_from, recipient_list )

    # info pass to html
    context = {
            'title': 'Request Of Quotation Details',
            'purchase_requisition_id' : purchase_requisition_id,
            'request_of_quotation_id' : roq_id,
            'vendor_id' : vendor_id,
            'rows' : items,
            'staff_info' : staff_info,
            'vendor_info' : vendor_info,
            'grand_total': grand_total,
            'time_created': current_time,
            'description' : description
        }

    return render(request,'RequestOfQuotation/requestofquotationdetails.html',context)

def requestofquotationhistorydetails(request):

    print(request.body)
    pk = request.GET['roq_id']
    request_of_quotation = RequestOfQuotation.objects.get(request_of_quotation_id = pk)
    items = RequestOfQuotationItem.objects.filter(request_of_quotation_id = pk)

    print(request_of_quotation.person_id)
    context = {

            'title': 'Request Of Quotation Details',
            'purchase_requisition_id' : request_of_quotation.purchase_requisition_id.pr_id,
            'request_of_quotation_id' : pk,
            'staff_id' : request_of_quotation.person_id.person_id,
            'vendor_id' : request_of_quotation.vendor_id.vendor_id,
            'rows' : items,
            'staff_info' : request_of_quotation.person_id,
            'vendor_info' : request_of_quotation.vendor_id,
            'grand_total': request_of_quotation.total_price,
            'time_created': request_of_quotation.time_created,
            'description' : request_of_quotation.description
        }
  
    return render(request,'RequestOfQuotation/requestofquotationhistorydetails.html',context)

def requestofquotationhistory(request):

    request_of_quotations = RequestOfQuotation.objects.all()

    context = {
            'title':'Request Of Quotation History',
            'rows':request_of_quotations
        }
    return render(request,'RequestOfQuotation/requestofquotationhistory.html',context)

