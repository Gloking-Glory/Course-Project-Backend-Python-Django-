from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_title', 'university', 'duration', 'location', 'fees', 'created_at', 'updated_at')
    search_fields = ('id', 'course_title', 'university')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    readonly_fields = ('id', 'created_at', 'updated_at')
    list_per_page = 50
    date_hierarchy = 'created_at'
