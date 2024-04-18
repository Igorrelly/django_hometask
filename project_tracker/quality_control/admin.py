from django.contrib import admin
from .models import FeatureRequest, BugReport

# Register your models here.

# Класс администратора для модели FeatureReauqest
@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'priority', 'status')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'

# Класс администратора для модели BugReport
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'priority', 'status')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'

    # Inline класс для модели FeatureRequest
class FeatureRequestInline(admin.TabularInline):
    model = FeatureRequest
    extra = 0
    fields = ('title', 'status', 'priority', 'created_at', 'updated_at')
    list_editable = ('status')
    readonly_fields = ('title', 'priority', 'created_at', 'updated_at')
    can_delete = True
    show_change_link = True

# Inline класс для модели BugReport
class BugReportInline(admin.TabularInline):
    model = BugReport
    extra = 0
    fields = ('title', 'status', 'priority', 'created_at', 'updated_at')
    list_editable = ('status')
    readonly_fields = ('title', 'priority', 'created_at', 'updated_at')
    can_delete = True
    show_change_link = True