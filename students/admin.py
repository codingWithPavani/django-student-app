from django.contrib import admin

# Register your models here.
from .models import Student 
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'age']
    search_fields = ['name', 'email']

admin.site.register(Student, StudentAdmin)
