from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'roll', 'name', 'marks')
    list_filter = ('name', 'id', 'roll', 'marks')
