from django.contrib import admin
from website1.models import Project
from website1.models import UserModel
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('proj_id', 'proj_title', 'proj_category', 'dept')
    search_fields = ['proj_title', 'proj_id']


class UserModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserModel._meta.fields if True]


admin.site.register(UserModel, UserModelAdmin)

admin.site.register(Project, ProjectAdmin)

