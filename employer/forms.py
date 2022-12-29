from django import forms
from .models import EmployeeModel

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = EmployeeModel
        fields = [ 'user', 'emp_id',  'gender', 'designation', 'age', 'department', 'first_name', 'middle_name', 'last_name' ]
        
