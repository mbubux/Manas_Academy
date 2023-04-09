from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

from apps.corecode.models import StudentClass




def increment_reg_number():
    last_reg = Student.objects.all().order_by('id').last()
    if not last_reg:
        return 'MAK0200'
    registration_number = last_reg.registration_number
    reg_int = int(registration_number.split('MAK')[-1])
    width = 4
    new_reg_int = reg_int + 1
    formatted = (width - len(str(new_reg_int))) * "0" + str(new_reg_int)
    new_reg_no = 'MAK' + str(formatted)
    return new_reg_no  


class Student(models.Model):
    STATUS_CHOICES = [("active", "Active"), ("inactive", "Inactive")]

    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]

    CATEGORY_CHOICE = [("General", "General"),
                       ("SC", "SC"),
                       ("ST", "ST"),  
                       ("OBC", "OBC"),
                       ("MOBC", "MOBC"), 
                       ("Others", "Others"),     
                       ]
    current_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active"
    )
    registration_number = models.CharField(max_length = 500, default = increment_reg_number, null = True, blank = True)
    # registration_number = models.CharField(max_length=200, unique=True)
    # surname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    fathers_name = models.CharField(max_length=200, blank=True)
    mothers_name= models.CharField(max_length=200, blank=True)

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")
    date_of_birth = models.DateField(default=timezone.now)
    current_class = models.ForeignKey(
        StudentClass, on_delete=models.SET_NULL, blank=True, null=True
    )
    date_of_admission = models.DateField(default=timezone.now)

    mobile_num_regex = RegexValidator(
        regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!"
    )
    parent_mobile_number = models.CharField(
        validators=[mobile_num_regex], max_length=13, blank=True
    )

    Students_Category = models.CharField(max_length=15, choices=CATEGORY_CHOICE, default="General")


    educational_block = models.CharField(max_length=200, default="Bhabanipur Block")
    cluster_name = models.CharField(max_length=200, blank=True)
    
    address = models.TextField(blank=True)

    district = models.CharField(max_length=200, default="Barpeta")
    state = models.CharField(max_length=200, default= "Assam")
    country = models.CharField(max_length=200, default= "India")
    
    pin_regex = RegexValidator(
        regex="^[0-9]{5,7}$", message="Entered Pin number isn't in a right format!"
    )
    pin=models.CharField(validators=[pin_regex], max_length=6, default=None)

    #Bank Details
    aadhar_no_regex = RegexValidator(
        regex="^[0-9]{11,13}$", message='please entere a correct Aadhar number !'
    )
    aadhaar_number = models.CharField(validators=[aadhar_no_regex], max_length= 15, blank=True)
    
    name_of_the_bank = models.CharField(max_length=200, blank=True)
    account_no_regex = RegexValidator(
        regex="^[0-9]{10,20}$", message="Entered bank account number isn't in a right format!"
    )
    account_no = models.CharField(validators=[account_no_regex], max_length= 15, blank=True)
    branch_name = models.CharField(max_length=200, blank=True)
    ifsc_code = models.CharField(max_length=10, blank=True)
    others = models.TextField(blank=True)
    student_photo = models.ImageField(blank=True, upload_to="students/student_photos/")
    birth_certificate =models.FileField(blank=True, null=True, upload_to="students/birth_certificate/")

    class Meta:
        ordering = ["firstname", "surname"]

    def __str__(self):
        return f"{self.firstname} {self.surname} ({self.registration_number})"

    def get_absolute_url(self):
        return reverse("student-detail", kwargs={"pk": self.pk})


class StudentBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to="students/bulkupload/")
