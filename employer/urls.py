from django.urls import path
from . import views
from django.views import View
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('employer/dashboard/', views.Dashboard.as_view(), name='employer/dashboard'),

    path('add_department/', views.AddDepartment.as_view(), name='add_department'),
    path('manage_department/', views.manage_department, name='manage_department'),

    path('add_designation/', views.AddDesignation.as_view(), name='add_designation'),
    path('manage_designation/', views.manage_designation, name='manage_designation'),

    path('add_employee/', views.Add_Employee.as_view(), name='add_employee'),
    path('manage_employee/', views.manage_employee, name='manage_employee'),
    
    path('add_user/', views.Add_User.as_view(), name='add_user'),
    path('manage_user/', views.manage_user, name='manage_user'),

    path('add_leave_type/', views.AddLeaveType.as_view(), name='add_leave_type'),
    path('manage_leave_type/', views.manage_leave_type, name='manage_leave_type'),
    
    path('all_leave/', views.all_leave, name='all_leave'),
    path('pending_leave/', views.pending_leave, name='pending_leave'),
    path('approve_leave/', views.approve_leave, name='approve_leave'),
    path('not_approve_leave/', views.not_approve_leave, name='not_approve_leave'),

    path('reports/', views.reports, name='reports'),
    path('leave_details/<str:id>', views.LeaveDetails.as_view(), name='leave_details'),
    path('leave_details/', views.LeaveDetails.as_view(), name='leave_details'),
    
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),

    path('delete_leave_type/<int:id>/', views.delete_leave, name='delete_leave'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),
    path('delete_employee/<int:id>/', views.delete_employee, name='delete_employee'),
    path('delete_department/<int:id>/', views.delete_department, name='delete_department'),
    path('delete_designation/<int:id>/', views.delete_designation, name='delete_designation'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)