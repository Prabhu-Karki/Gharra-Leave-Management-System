from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import *
from .forms import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from employee.models import *

class IndexView(View):
    def get(self, request):
        return render(request, 'login.html')

class Dashboard(View):
    @method_decorator(login_required(login_url='accounts/login/'))
    def get(self, request):
        category = request.user.category
        context = {
            'profile': request.user.profile,
            'notifications': ApplyLeave.objects.filter(status='Pending'),
            'total_notifi': len(ApplyLeave.objects.filter(status='Pending')),
            'dashboard_status': 'active',
            'leaves' : ApplyLeave.objects.all(),
            'approved' : len(ApplyLeave.objects.filter(status='Approve')),
            'pending' : len(ApplyLeave.objects.filter(status='Pending')),
            'rejected': len(ApplyLeave.objects.filter(status='Rejected')),
            'total_employee': len(EmployeeModel.objects.all()),
            'employee_leave': len(ApplyLeave.objects.filter(status='Approve')),
        }
        if category == 'Admin':
            return render(request, 'index.html', context)
        else:
            return redirect('employee/dashboard', context)
        
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(password = password, username= email)

        if user is not None:
            auth.login(request, user)
            category = request.user.category
            emp = User.objects.filter(username= request.user.username, is_employee=True)
            if category == 'Admin':
                return redirect('/employer/dashboard/')

            elif category == 'Staff' and emp:
                return redirect('/employee/dashboard/')

            else:
                messages.info(request, 'You should either be Staff or Admin to login.')
                return render(request, 'login.html')

        else:
            messages.info(request, 'Invalid Credintials. Please try again')
        return render(request, 'login.html')

class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect('/')

class Add_Employee(View):
    @method_decorator(login_required(login_url='accounts/login/'))
    def get(self, request):
        context = {
            'users': User.objects.filter(is_employee= False),
            'notifications': ApplyLeave.objects.filter(status='Pending'),
            'total_notifi': len(ApplyLeave.objects.filter(status='Pending')),
            'profile': request.user.profile,
            'emp_status': 'active',
            'leaves' : ApplyLeave.objects.all(),
        }
        return render(request, 'add_employee.html', context)

    def post(self, request):
        emp_username = request.POST['emp_user']
        emp_user = User.objects.get(username=emp_username)
        emp_id   = request.POST['emp_id']
        department = request.POST['department']
        designation = request.POST['designation']
        gender = request.POST['gender']
        age = request.POST['age']
        fname = request.POST['fname']
        mname = request.POST['mname']
        lname = request.POST['lname']
        EmployeeModel(user=emp_user, emp_id = emp_id, department = department, designation=designation, gender=gender, age=age, first_name=fname, middle_name=mname, last_name=lname).save()
        filtration = User.objects.filter(username=emp_username)
        filtration.update(is_employee=True)
        return redirect('employer/dashboard')
       
class AddDepartment(View):
    @method_decorator(login_required(login_url='accounts/login/'))
    def get(self, request):
        context = {
            'profile': request.user.profile,
            'total_notifi': len(ApplyLeave.objects.filter(status='Pending')),
            'notifications': ApplyLeave.objects.filter(status='Pending'),
            'dept_status': 'active',
            'leaves' : ApplyLeave.objects.all(),
        }
        return render(request, 'add_department.html', context)

    def post(self, request):
        short_form = request.POST['short_form']
        full_form = request.POST['full_form']
        Department(short_form=short_form, full_form=full_form).save()
        return redirect('manage_department')

@login_required
def manage_department(request):
    context = {
        'profile': request.user.profile,
        'total_notifi': len(ApplyLeave.objects.filter(status='Pending')),
        'notifications': ApplyLeave.objects.filter(status='Pending'),
        'dept_status': 'active',
        'leaves' : ApplyLeave.objects.all(),
        'departments': Department.objects.all(),
    }
    return render(request, 'manage_department.html', context)

class AddDesignation(View):
    @method_decorator(login_required(login_url='accounts/login/'))
    def get(self, request):
        context = {
        'profile': request.user.profile,
        'design_status': 'active',
        'total_notifi': len(ApplyLeave.objects.filter(status='Pending')),
        'notifications': ApplyLeave.objects.filter(status='Pending'),
        'leaves' : ApplyLeave.objects.all(),
    }
        return render(request, 'add_designation.html', context)

    def post(self, request):
        designation = request.POST['designation']
        description = request.POST['description']
        Designation(designation=designation, description=description).save()
        return redirect('manage_designation')

@login_required
def manage_designation(request):
    context = {
        'profile': request.user.profile,
        'total_notifi': len(ApplyLeave.objects.filter(status='Pending')),
        'notifications': ApplyLeave.objects.filter(status='Pending'),
        'design_status': 'active',
        'leaves' : ApplyLeave.objects.all(),
        'designations': Designation.objects.all(),
    }
    return render(request, 'manage_designation.html', context)

@login_required
def manage_employee(request):
    employees = EmployeeModel.objects.all()
    context = {
        'employees' : employees,
        'total_notifi': len(ApplyLeave.objects.filter(status='Pending')),
        'profile': request.user.profile,
        'notifications': ApplyLeave.objects.filter(status='Pending'),
        'emp_status': 'active',
        'leaves' : ApplyLeave.objects.all(),
    }
    return render(request, 'manage_employee.html', context)

class AddLeaveType(View):
    @method_decorator(login_required(login_url='accounts/login/'))
    def get(self, request):
        context = {
        'profile': request.user.profile,
        'total_notifi': len(ApplyLeave.objects.filter(status='Pending')),
        'notifications': ApplyLeave.objects.filter(status='Pending'),
        'leave_status': 'active',
        'leaves' : ApplyLeave.objects.all(),
    }
        return render(request, 'add_leave_type.html', context)

    def post(self, request):
        leave_type = request.POST['leave_type']
        days_allowed = request.POST['days_allowed']
        LeaveType.objects.create(leave_type=leave_type, days_allowed=days_allowed)
        return redirect('manage_leave_type')

@login_required
def manage_leave_type(request):
    context = {
        'profile': request.user.profile,
        'total_notifi': len(ApplyLeave.objects.filter(status='Pending')),
        'notifications': ApplyLeave.objects.filter(status='Pending'),
        'leave_status': 'active',
        'leaves' : ApplyLeave.objects.all(),
        'leave_types': LeaveType.objects.all(),
    }
    return render(request, 'manage_leave_type.html', context)

@login_required
def all_leave(request):
    context = {
        'profile': request.user.profile,
        'leavem_status': 'active',
        'leaves' : ApplyLeave.objects.all(),
        'total_notifi': len(ApplyLeave.objects.filter(status='Pending')),
        'notifications': ApplyLeave.objects.filter(status='Pending'),
    }
    return render(request, 'all_leave.html', context)

@login_required
def pending_leave(request):
    context = {
        'profile': request.user.profile,
        'total_notifi': len(ApplyLeave.objects.filter(status='Pending')),
        'notifications': ApplyLeave.objects.filter(status='Pending'),
        'leavem_status': 'active',
        'leaves' : ApplyLeave.objects.all(),
        'pendings': ApplyLeave.objects.filter(status='Pending')
    }
    return render(request, 'pending_leave.html', context)

@login_required
def approve_leave(request):
    context = {
        'profile': request.user.profile,
        'total_notifi': len(ApplyLeave.objects.filter(status='Pending')),
        'notifications': ApplyLeave.objects.filter(status='Pending'),
        'leavem_status' : 'active',
        'leaves' : ApplyLeave.objects.all(),
        'approved': ApplyLeave.objects.filter(status='Approved')
    }
    return render(request, 'approve_leave.html', context)

@login_required
def not_approve_leave(request):
    context = {
        'profile': request.user.profile,
        'total_notifi': len(ApplyLeave.objects.filter(status='Pending')),
        'notifications': ApplyLeave.objects.filter(status='Pending'),
        'leavem_status': 'active',
        'leaves' : ApplyLeave.objects.all(),
        'rejected': ApplyLeave.objects.filter(status='Rejected')
    }
    return render(request, 'not_approve_leave.html', context)


class Add_User(View):
    @method_decorator(login_required(login_url='accounts/login/'))
    def get(self, request):
        context = {
        'profile': request.user.profile,
        'notifications': ApplyLeave.objects.filter(status='Pending'),
        'total_notifi': len(ApplyLeave.objects.filter(status='Pending')),
        'user_status': 'active',
    }
        return render(request, 'add_user.html', context)

    def post(self, request):
        full_name = request.POST['full_name']
        phone= request.POST['phone']
        email = request.POST['email']
        username= request.POST['username']
        password = request.POST['password']
        category = request.POST['category']
        profile = request.POST['profile']
        user = User.objects.create(full_name=full_name, profile=profile, phone_number=phone, email=email, username=username, category=category)
        if user is not None:
            user.set_password(password)
            user.is_active = True
            user.save()
            category = request.user.category
            if category == 'Admin':
                user.is_staff = True
                user.save()
            return redirect('manage_user')
        else:
            return redirect('add_user')

@login_required     
def manage_user(request):
    users = User.objects.all()
    context = {
        'profile': request.user.profile,
        'total_notifi': len(ApplyLeave.objects.filter(status='Pending')),
        'notifications': ApplyLeave.objects.filter(status='Pending'),
        'users': users,
        'user_status': 'active',
        'leaves' : ApplyLeave.objects.all(),

    }
    return render(request, 'manage_user.html', context)

@login_required
def reports(request):
    context = {
        'profile': request.user.profile,
        'total_notifi': len(ApplyLeave.objects.filter(status='Pending')),
        'notifications': ApplyLeave.objects.filter(status='Pending'),
        'reports_status': 'active',
        'leaves' : ApplyLeave.objects.all(),
        'data_1' : len(ApplyLeave.objects.filter(status='Approved')),
        'data_2' : len(ApplyLeave.objects.filter(status='Pending')),
        'data_3' : len(ApplyLeave.objects.filter(status='Rejected')),
    }
    return render(request, 'reports.html', context)

class LeaveDetails(View):
    @method_decorator(login_required(login_url='accounts/login/'))
    def get(self, request, id):
        context = {
        'profile': request.user.profile,
        'total_notifi': len(ApplyLeave.objects.filter(status='Pending')),
        'notifications': ApplyLeave.objects.filter(status='Pending'),
        'leavem_status': 'active',
        'leaves' : ApplyLeave.objects.filter(id = id)
        }
        return render(request, 'leave_details.html', context)

    def post(self, request, id):
        value = request.POST['value']
        ApplyLeave.objects.filter(id = id).update(status=value)
        return redirect('all_leave')

@login_required
def delete_leave(request, id):
    LeaveType.objects.filter(id=id).delete()
    return redirect('manage_leave_type')

@login_required
def delete_user(request, id):
    User.objects.filter(id=id).delete()
    return redirect('manage_user')

@login_required
def delete_employee(request, id):
    EmployeeModel.objects.filter(id=id).delete()
    return redirect('manage_employee')

@login_required
def delete_department(request, id):
    Department.objects.filter(id=id).delete()
    return redirect('manage_department')

@login_required
def delete_designation(request, id):
    Designation.objects.filter(id=id).delete()
    return redirect('manage_designation')