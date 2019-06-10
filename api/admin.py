# _*_ coding:utf-8 _*_
from django.contrib import admin

# Register your models here.

from api.models import App, ApiLog


class AppAdmin(admin.ModelAdmin):
    model = App
    search_fields = ['uuid']
    list_display = ['user', 'kind', 'port', 'create_time']


admin.site.register(App, AppAdmin)


class ApiLogAdmin(admin.ModelAdmin):
    model = ApiLog
    list_display = ['uuid', 'behavior', 'create_time']


admin.site.register(ApiLog, ApiLogAdmin)

