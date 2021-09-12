from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactList(admin.ModelAdmin):
    model = Contact
    list_display = ['name' , 'email' ,'subject']
admin.site.register(Contact , ContactList)