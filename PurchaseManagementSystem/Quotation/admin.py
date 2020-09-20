from django.contrib import admin

# Register your models here.
from Quotation.models import Quotation,QuotationItem

admin.site.register(Quotation)
admin.site.register(QuotationItem)