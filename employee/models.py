from django.db import models
from employer.models import *
import uuid
STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Approved', "Approved"),
    ('Rejected', "Rejected"),
)

# Create your models here.
class ApplyLeave(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, null=True)
    leave_from = models.DateField()
    leave_to = models.DateField()
    reference_no = models.CharField(max_length=50)
    leave_type = models.CharField(max_length=50)
    posting_date = models.DateField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='Pending')
    total_leave = models.PositiveSmallIntegerField(default='0')

