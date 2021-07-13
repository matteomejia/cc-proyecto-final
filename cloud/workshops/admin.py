from django.contrib import admin

from .models import Workshop, Topic
# Register your models here.


class TopicAdmin(admin.ModelAdmin):
    list_display = ['name']

class WorkshopAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', 'start_date')}
    list_display = ['title', 'start_date', 'status']


admin.site.register(Topic, TopicAdmin)
admin.site.register(Workshop, WorkshopAdmin)