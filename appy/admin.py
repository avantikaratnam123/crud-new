
from django.contrib import admin
from  . models import  * 


# Register your models here.

'''@admin.register((Register))
class RegisterModelAdmin(admin.ModelAdmin):
    list_display =['id','name','email','phone','password']'''
admin.site.register(Register)