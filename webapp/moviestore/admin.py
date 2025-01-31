from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie_title', 'user', 'rating', 'created_at', 'updated_at')  # Columns to display
    list_filter = ('rating', 'created_at', 'updated_at')  # Filters for the list view
    search_fields = ('movie_title', 'review_text', 'user__username')  # Search functionality
    readonly_fields = ('created_at', 'updated_at')  # Prevent editing of timestamps

    # Add actions for bulk operations
    actions = ['delete_selected_reviews']

    def delete_selected_reviews(self, request, queryset):
        queryset.delete()
    delete_selected_reviews.short_description = "Delete selected reviews"

admin.site.register(Review, ReviewAdmin)