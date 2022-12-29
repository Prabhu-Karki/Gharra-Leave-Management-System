from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(ApplyLeave)
class ApplyLeave(admin.ModelAdmin):
    list_display = ['id', ]