from django.contrib import admin

from response.models import Response


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    pass
