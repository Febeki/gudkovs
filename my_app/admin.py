from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from . import models


User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', )}),
    )
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('role', )}),
    )


@admin.register(models.FirstName)
class FirstNameAdmin(admin.ModelAdmin):
    list_display = ('nominative', 'genitive', 'dative', 'accusative', 'instrumental', 'prepositional', 'latin')


@admin.register(models.LastName)
class FirstNameAdmin(admin.ModelAdmin):
    list_display = ('nominative', 'genitive', 'dative', 'accusative', 'instrumental', 'prepositional', 'latin')


@admin.register(models.Patronymic)
class FirstNameAdmin(admin.ModelAdmin):
    list_display = ('nominative', 'genitive', 'dative', 'accusative', 'instrumental', 'prepositional', 'latin')


@admin.register(models.Snils)
class SnilsAdmin(admin.ModelAdmin):
    list_display = ('number',)


@admin.register(models.Passport)
class PassportAdmin(admin.ModelAdmin):
    list_display = ('series', 'number', 'issued_date', 'issued_by', 'department_code')  #  , 'is_valid'


@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role',)


@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic', 'role', 'passport', 'snils', 'email', 'phone_number', 'birthday')
    list_filter = ('role', 'name', 'surname')
    search_fields = ('name', 'surname', 'patronymic', 'email', 'phone_number')


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('member', 'start_time', 'end_time', 'project', 'lunch_break')