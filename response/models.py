from django.db import models
from django.conf import settings
from survey.models import Field


class Response(models.Model):
    respondent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Field, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.answer

