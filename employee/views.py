from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import *
from employer.models import *
# Create your views here.
from datetime import datetime

class EmployeeDashboard(View):
    def get(self, request):
        # total_leave = (ApplyLeave.leave_from - ApplyLeave.leave_to).days
        apply_leave = ApplyLeave.objects.filter(employee=self.request.user.employeemodel, status= 'Approved')
        
        total_leave = 0
        if apply_leave:
            for leave in apply_leave:
                leave_from_datetime = datetime.combine(leave.leave_from, datetime.min.time())
                leave_to_datetime = datetime.combine(leave.leave_to, datetime.min.time())
                total_leave = (leave_to_datetime - leave_from_datetime).days
            
        context= {
            'employee': EmployeeModel.objects.filter(user=self.request.user),
            'dash_status': 'active',
            'approved' : len( ApplyLeave.objects.filter(user= self.request.user, status='Approve')),
            'pending' : len(ApplyLeave.objects.filter(user= self.request.user, status='Pending')),
            'rejected': len(ApplyLeave.objects.filter(user= self.request.user, status='Rejected')),
            'total_leave': total_leave,
        }
        return render(request, 'employee.html', context)

class ApplyLeaves(View):
    def get(self, request):
        context= {
            'employee': EmployeeModel.objects.filter(user=self.request.user),
            'apply_status': 'active',
            'leave_types': LeaveType.objects.all()
        }
        return render(request, 'apply_leave.html', context)

    def post(self, request):
        # employee = request.POST['']
        ref_no = request.POST['ref_no']
        leave_from = request.POST['leave_from']
        leave_to = request.POST['leave_to']
        leave_type = request.POST['leave_type']
        ApplyLeave(reference_no = ref_no, employee=self.request.user.employeemodel, leave_from = leave_from, leave_to = leave_to, leave_type = leave_type).save()
        return redirect('employee/dashboard')

def update(request):
    return render(request, 'update.html')

def update_password(request):
    return render(request, 'update_password.html')

class LeaveStatus(View):
    def get(self, request):
        context = {
            'lea_status': 'active',
            'leave_status': ApplyLeave.objects.filter(employee=self.request.user.employeemodel)
        }
        return render(request, 'leave_status.html', context)
