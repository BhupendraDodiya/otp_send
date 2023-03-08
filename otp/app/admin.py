from django.contrib import admin
from .models import reg
# Register your models here.
@admin.register((reg))
class regModelAdmin(admin.ModelAdmin):
    list_display= ['id','Name','City','Email']
