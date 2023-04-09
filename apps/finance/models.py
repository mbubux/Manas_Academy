from django.db import models
from django.urls import reverse
from django.utils import timezone

from apps.corecode.models import AcademicSession, AcademicTerm, StudentClass, fee_type
from apps.students.models import Student


class Invoice(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
    term = models.ForeignKey(AcademicTerm, on_delete=models.CASCADE)
    class_for = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    balance_from_previous_term = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=[("active", "Active"), ("closed", "Closed")],
        default="active",
    )
    discount = models.IntegerField(default=0)

    class Meta:
        ordering = ["student", "term"]

    def __str__(self):
        return f"{self.student}"

    def balance(self):
        payable = self.total_amount_payable()
        paid = self.total_amount_paid()
        return payable - paid - self.discount

    def amount_payable(self):
        items = InvoiceItem.objects.filter(invoice=self)
        total = 0
        for item in items:
            total += item.amount
        return total

    def total_amount_payable(self):
        return self.balance_from_previous_term + self.amount_payable() 

    def total_amount_paid(self):
        receipts = Receipt.objects.filter(invoice=self)
        amount = 0
        for receipt in receipts:
            amount += receipt.amount_paid
        return amount

    def get_absolute_url(self):
        return reverse("invoice-detail", kwargs={"pk": self.pk})


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.ForeignKey(fee_type, on_delete=models.CASCADE)
    amount = models.IntegerField()



def increment_invoice_number():
    last_invoice = Receipt.objects.all().order_by('id').last()
    if not last_invoice:
        return 'MA00001'
    invoice_no = last_invoice.invoice_no
    invoice_int = int(invoice_no.split('MA')[-1])
    width = 5
    new_invoice_int = invoice_int + 1
    formatted = (width - len(str(new_invoice_int))) * "0" + str(new_invoice_int)
    new_invoice_no = 'MA' + str(formatted)
    return new_invoice_no 

class Receipt(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount_paid = models.IntegerField()
    date_paid = models.DateField(default=timezone.now)
    comment = models.CharField(max_length=200, blank=True)
    invoice_no = models.CharField(max_length=500, default=increment_invoice_number )

    def __str__(self):
        return f"Receipt on {self.date_paid}"
