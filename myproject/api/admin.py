from django.contrib import admin
from . models import *
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','email','city')

admin.site.register(Student,StudentAdmin)