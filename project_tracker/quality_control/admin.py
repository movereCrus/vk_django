from django.contrib import admin
from .models import(BugReport, FeatureRequest, Project, Task)


@admin.action(description="Mark selected bug reports as resolved")
def make_resolved(modeladmin, request, queryset):
    queryset.update(status="Completed")


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project', 'task')
    search_fields = ('title', 'description')
    fieldsets = (
        ('Standard info', {
            'fields': ('title',)
        }),
        ('Description', {
            'fields': ('description', ('status', 'priority', 'project', 'task'))
        }),
    )
    ordering = ('created_at',)
    date_hierarchy = 'created_at'
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')
    actions = [make_resolved]


@admin.register(FeatureRequest)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'priority', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project', 'task')
    search_fields = ('title', 'description')
    fieldsets = (
        ('Standard info', {
            'fields': ('title',)
        }),
        ('Description', {
            'fields': ('description', ('status', 'priority', 'project', 'task'))
        }),
    )
    ordering = ('created_at',)
    date_hierarchy = 'created_at'
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')

