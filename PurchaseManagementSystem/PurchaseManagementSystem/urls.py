"""
Definition of urls for PurchaseManagementSystem.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views
import PurchaseOrder.views
import PurchaseRequisition.views
import RequestOfQuotation.views
import Quotation.views
import DeliveryOrder.views
import Invoice.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    #admin
    url(r'^admin/', admin.site.urls, name="admin"),

    #app
    url(r'^$', app.views.userlogin, name='userlogin'),
    url(r'^menu', app.views.menu, name="menu"),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    #purchase requisition
    url(r'^purchaserequisitionform$', PurchaseRequisition.views.purchaserequisitionform, name="purchase_requisition_form"),
    url(r'^purchaserequisitionconfirmation', PurchaseRequisition.views.purchaserequisitionconfirmation, name="confirm_purchase_requisition"),
    url(r'^purchaserequisitiondetails', PurchaseRequisition.views.purchaserequisitiondetails, name="purchase_requisition_details"),
    url(r'^purchaserequisitionhistorydetails', PurchaseRequisition.views.purchaserequisitionhistorydetails, name='purchase_requisition_history_details'),
    url(r'^purchaserequisitionhistory', PurchaseRequisition.views.purchaserequisitionhistory, name="purchase_requisition_history"),

    #request of quotation
    url(r'^requestofquotationform$', RequestOfQuotation.views.requestofquotationform, name="request_of_quotation_form"),
    url(r'^fillingrequestofquotation', RequestOfQuotation.views.fillingrequestofquotation, name="fill_request_of_quotation_form"),
    url(r'^requestofquotationconfirmation', RequestOfQuotation.views.requestofquotationconfirmation, name="confirm_request_of_quotation"),
    url(r'^requestofquotationdetails', RequestOfQuotation.views.requestofquotationdetails, name="request_of_quotation_details"),
    url(r'^requestofquotationhistorydetails', RequestOfQuotation.views.requestofquotationhistorydetails, name='request_of_quotation_history_details'),
    url(r'^requestofquotationhistory', RequestOfQuotation.views.requestofquotationhistory, name="request_of_quotation_history"),

    #quotation
    url(r'^quotationform$', Quotation.views.quotationform, name="quotation_form"),
    url(r'^fillingquotation', Quotation.views.fillingquotation, name="fill_quotation_form"),
    url(r'^quotationconfirmation', Quotation.views.quotationconfirmation, name="confirm_quotation"),
    url(r'^quotationdetails', Quotation.views.quotationdetails, name="quotation_details"),
    url(r'^quotationhistorydetails', Quotation.views.quotationhistorydetails, name='quotation_history_details'),
    url(r'^quotationhistory', Quotation.views.quotationhistory, name="quotation_history"),

    #purchase order
    url(r'^purchaseorderform$', PurchaseOrder.views.purchaseorderform, name="purchase_order_form"),
    url(r'^fillingpurchaseorder', PurchaseOrder.views.fillingpurchaseorder, name="fill_purchase_order_form"),
    url(r'^purchaseorderconfirmation', PurchaseOrder.views.purchaseorderconfirmation, name="confirm_purchase_order"),
    url(r'^purchaseorderdetails', PurchaseOrder.views.purchaseorderdetails, name="purchase_order_details"),
    url(r'^purchaseorderhistorydetails', PurchaseOrder.views.purchaseorderhistorydetails, name='purchase_order_history_details'),
    url(r'^purchaseorderhistory', PurchaseOrder.views.purchaseorderhistory, name="purchase_order_history"),

    #delivery order
    url(r'^deliveryorderform$', DeliveryOrder.views.deliveryorderform, name="delivery_order_form"),
    url(r'^fillingdeliveryorder', DeliveryOrder.views.fillingdeliveryorder, name="fill_delivery_order_form"),
    url(r'^deliveryorderconfirmation', DeliveryOrder.views.deliveryorderconfirmation, name="confirm_delivery_order"),
    url(r'^deliveryorderdetails', DeliveryOrder.views.deliveryorderdetails, name="delivery_order_details"),
    url(r'^deliveryorderhistorydetails', DeliveryOrder.views.deliveryorderhistorydetails, name='delivery_order_history_details'),
    url(r'^deliveryorderhistory', DeliveryOrder.views.deliveryorderhistory, name="delivery_order_history"),

    #Invoice
    url(r'^invoiceform$', Invoice.views.invoiceform, name="invoiceform"),
    url(r'^fillinginvoice', Invoice.views.fillinginvoice, name="fill_invoice_form"),
    url(r'^invoiceconfirmation', Invoice.views.invoiceconfirmation, name="confirm_invoice"),
    url(r'^invoicedetails', Invoice.views.invoicedetails, name="invoice_details"),
    url(r'^invoicehistorydetails', Invoice.views.invoicehistorydetails, name='invoice_history_details'),
    url(r'^invoicehistory', Invoice.views.invoicehistory, name="invoice_history"),
]
