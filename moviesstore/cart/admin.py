from django.contrib import admin
from .models import Order, Item
class ItemInline(admin.TabularInline):
    model = Item
    extra = 1
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total', 'date', 'get_movies')
    search_fields = ('user__username', 'id')
    list_filter = ('date',)
    inlines = [ItemInline]
    def get_movies(self, obj):
        return ", ".join([movie.name for movie in obj.movie.all()])
    get_movies.short_description = 'Movies'

admin.site.register(Order, OrderAdmin)
admin.site.register(Item)