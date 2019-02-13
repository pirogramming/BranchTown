from django.contrib import admin
from .models import Response
# Register your models here.

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    pass
