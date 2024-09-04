from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active']    


admin.site.register(User, UserAdmin)