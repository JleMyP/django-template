from django.contrib.admin import site
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Персональная информация', {
            'fields': (('first_name', 'last_name', 'middle_name'), 'email', 'phone')
        }),
        ('Права', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            'classes': ('collapse',),
        }),
        ('Даты', {
            'fields': (('last_login', 'date_joined'),),
            'classes': ('collapse',)
        }),
    )
    list_display = ('username', 'email', 'phone', 'first_name', 'last_name', 'middle_name',
                    'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'middle_name', 'email', 'phone')
    change_form_template = 'loginas/change_form.html'
    actions_on_bottom = True


site.register(get_user_model(), CustomUserAdmin)
site.register(Permission)
