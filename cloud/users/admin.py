from django.contrib import admin

from .models import User, Student

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'last_login', 'date_joined']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'school', 'parent']
    ordering = ['pk']


admin.site.register(User, UserAdmin)
admin.site.register(Student, StudentAdmin)