from django.contrib import admin
from .models import Survey, Field, Multiple_Choice


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    pass


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ['question', 'type', 'form']


@admin.register(Multiple_Choice)
class Multiple_ChoiceAdmin(admin.ModelAdmin):
    list_display = ['field', 'choice1', 'choice2', 'choice3']


