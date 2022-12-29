from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    is_employee = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    phone_number = models.PositiveIntegerField(null=True, blank=True, default=1234567890)
    full_name = models.CharField(max_length=80, blank = False, default='Anonymous')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, default='Admin')
    profile = models.ImageField(upload_to='profile_pic', blank=True, default='profile_pic/admin.png')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

class EmployeeModel(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    emp_id =  models.CharField(max_length=50)
    department = models.CharField( max_length=50)
    designation = models.CharField( max_length=50)
    gender = models.CharField( max_length=50)
    age = models.PositiveIntegerField()
    first_name = models.CharField(max_length=70)
    middle_name = models.CharField(max_length=70, blank=True)
    last_name = models.CharField(max_length=70)
    date_registered = models.DateField(auto_now_add=True)

class LeaveType(models.Model):
    leave_type = models.CharField(max_length=100)
    days_allowed = models.PositiveSmallIntegerField()
    date_created = models.DateField(auto_now_add=True)

class Designation(models.Model):
    designation = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True)

class Department(models.Model):
    short_form = models.CharField(max_length=10)
    full_form = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
