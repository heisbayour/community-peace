from django.contrib import admin
from .models import Document, ArchiveItem

@admin.action(description='Mark selected documents as approved')
def make_approved(modeladmin, request, queryset):
    queryset.update(approved=True)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'approved')
    list_filter = ('approved', 'uploaded_at')
    actions = [make_approved]
    search_fields = ('title', 'tags')


@admin.register(ArchiveItem)
class ArchiveItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'status', 'media_type')
    list_filter = ('status', 'media_type', 'date')
    search_fields = ('title', 'tags')
