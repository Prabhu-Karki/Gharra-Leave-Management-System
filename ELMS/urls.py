from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employer.urls')),
    path('', include('employee.urls')),
]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('info.urls')),
#     path('info/', include('info.urls')),
#     path('api/', include('apis.urls')),

# ]