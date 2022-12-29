from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'first_name' )


# @admin.register(UserProfile)
# class UserProfile(admin.ModelAdmin):
#     list_display = ('id', 'full_name' )

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'id']

@admin.register(LeaveType)
class LeaveType(admin.ModelAdmin):
    list_display = ['id', 'leave_type', 'days_allowed']