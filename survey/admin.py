from django.contrib import admin
from .models import Survey, Field, Question, Choice


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    pass


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ['type', 'form']


@admin.register(Question)
class Question(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date']


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'choice_text', 'votes']


