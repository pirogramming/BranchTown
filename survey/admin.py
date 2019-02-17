from django.contrib import admin
from .models import Survey, Field, MultipleChoice


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    pass


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    pass


@admin.register(MultipleChoice)
class MultipleChoiceAdmin(admin.ModelAdmin):
    pass

