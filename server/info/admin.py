from django.contrib import admin

# Register your models here.
class DbImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_added', 'date_modified')
    list_filter = ('date_added', 'date_modified')
    search_fields = ('name',)
    ordering = ('-date_added',)