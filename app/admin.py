from django.contrib import admin
from .models import User, Task

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active']    


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'due_date', 'priority', 'status']


admin.site.register(User, UserAdmin)
admin.site.register(Task, TaskAdmin)