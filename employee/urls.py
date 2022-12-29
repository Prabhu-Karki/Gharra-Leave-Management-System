from django.urls import path
from . import views

urlpatterns = [
    path('employee/dashboard/', views.EmployeeDashboard.as_view(), name='employee/dashboard'),

    path('employee/apply_leave/', views.ApplyLeaves.as_view(), name='apply_leave'),
    path('employee/leave_status/', views.LeaveStatus.as_view(), name='leave_status'),

    path('employee/update/', views.update, name='update'),
    path('employee/update_password/', views.update_password, name='update_password'),

]
