from django.contrib import admin
from .models import Project, Client, ContactForm, NewsletterSubscription
from django.utils.html import format_html

admin.site.site_header = "RealTrust"


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'description', 'created_at', 'image_tag')
    readonly_fields = ('image_tag',)
    search_fields = ('name', 'designation')
    list_filter = ('designation', 'created_at')
    ordering = ('-created_at',)

    def image_tag(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="height: 100px;"/>')
        return "No Image"

    image_tag.short_description = 'Image Preview'

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'image_tag')  # Display details and image
    readonly_fields = ('image_tag',)  # Show image preview in detail view
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    def image_tag(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="height: 100px;"/>')
        return "No Image"

    image_tag.short_description = 'Image Preview'


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'mobile_number', 'city', 'submitted_at')
    list_filter = ('city', 'submitted_at')  # Filters for easier navigation
    search_fields = ('full_name', 'email', 'mobile_number', 'city')  # Search functionality
    ordering = ('-submitted_at',)  # Order by latest submissions

@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    list_filter = ('subscribed_at',)  # Filter by subscription date
    search_fields = ('email',)  # Search by email
    ordering = ('-subscribed_at',)  # Order by latest subscriptions
