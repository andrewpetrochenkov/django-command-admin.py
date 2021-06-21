from django.contrib import admin
from django.utils.timesince import timesince
from django.urls import include, path

class CallAdmin(admin.ModelAdmin):
    list_display = ['id','app','name','stdout','started_at','finished_at','duration','timesince']
    list_display_links =[]
    list_filter = ['name',]
    search_fields = ['name']

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def duration(self, obj):
        if obj.started_at and obj.finished_at:
            s = str(obj.finished_at - obj.started_at)
            return s.split('.')[0] + '.' + s.split('.')[1][0:3] if '.' in s else s
    duration.short_description = 'duration'

    def timesince(self, obj):
        return timesince(obj.finished_at).split(',')[0]+' ago' if obj.finished_at else None
    timesince.short_description = ''
