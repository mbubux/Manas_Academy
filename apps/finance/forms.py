from django.forms import inlineformset_factory, modelformset_factory
from django import forms

from .models import Invoice, InvoiceItem, Receipt

InvoiceItemFormset = inlineformset_factory(
    Invoice, InvoiceItem, fields=["description", "amount"], extra=1, can_delete=True
)

InvoiceReceiptFormSet = inlineformset_factory(
    Invoice,
    Receipt,
    fields=("amount_paid", "date_paid", "comment"),
    extra=0,
    can_delete=True,
)

Invoices = modelformset_factory(Invoice, exclude=(), extra=4)

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'