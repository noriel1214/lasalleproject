from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','city', 'state', 'is_published', 'price', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title','city', 'state', 'zipcode', 'price', 'description', 'address')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)

admin.site.site_header = "Philly Real Estate Portal Admin"
admin.site.site_title = "Philly Real Estate Portal Admin Portal"
admin.site.index_title = "Welcome to Philly Real Estate Portal"
