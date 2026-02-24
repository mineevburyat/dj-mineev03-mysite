from django.contrib import admin

from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'source', 'created_at', 'get_short_url']
    list_filter = ['source', 'created_at', ]
    search_fields = ['email', 'name', 'telegram']
    readonly_fields = ['created_at', 'ip_address', 'user_agent']
    
    fieldsets = (
        ('Основное', {
            'fields': ('name', 'email', 'telegram')
        }),
        ('Отслеживание', {
            'fields': ('source', 'url', 'ip_address', 'user_agent')
        }),
        
        ('Дата', {
            'fields': ('created_at',)
        }),
    )
    
    def get_short_url(self, obj):
        if obj.url:
            return obj.url[:50] + '...' if len(obj.url) > 50 else obj.url
        return '-'
    get_short_url.short_description = 'URL'
