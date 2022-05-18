from django.contrib import admin
from . import models

class CategoryAdmin(admin.ModelAdmin):
    list_display     = ['cat_name', 'ordering', 'status']
    search_fields    = ['title']
    list_filter      = ['status']
    
class ServiceAdmin(admin.ModelAdmin):
    list_display     = ['catagory','title','title_url','photo','views','ordering', 'status']
    search_fields    = ['title']
    list_filter      = ['status']
    
class WebseoAdmin(admin.ModelAdmin):
    list_display     = ['index_meta_title', 'status']
    list_filter      = ['status']
    
class PrivacyAdmin(admin.ModelAdmin):
    list_display     = ['pri_details']

class AboutusAdmin(admin.ModelAdmin):
    list_display     = ['about_details']

class TermAdmin(admin.ModelAdmin):
    list_display     = ['term_details']

class ContactAdmin(admin.ModelAdmin):
    list_display     = ['contact_details']

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.SeoContent, WebseoAdmin)
admin.site.register(models.Privacy, PrivacyAdmin)
admin.site.register(models.Aboutus, AboutusAdmin)
admin.site.register(models.Term, TermAdmin)
admin.site.register(models.Contact, ContactAdmin)