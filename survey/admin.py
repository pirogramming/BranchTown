from django.contrib import admin
from .models import Survey, Field, MultipleChoice, Index, TextAnswer


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    pass


@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    pass


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ['type', 'question', 'form']


@admin.register(MultipleChoice)
class MultipleChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text', 'votes']


@admin.register(TextAnswer)
class TextAnswerAdmin(admin.ModelAdmin):
    pass


