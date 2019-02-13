from django.db import models
from django.conf import settings
from tag.models import Tag


class Survey(models.Model):
    STATUS_CHOICES = (
        ('o', 'ongoing'),
        ('c', 'complete'),
        # TODO 다른 다양한 status 추가
    )
    title = models.CharField(max_length=100)
    subtitle = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title


class Field(models.Model):
    FIELD_TYPE = (
        ('1', '객관식'),
        ('2', '주관식'),
        ('3', '단답식'),
    )
    type = models.CharField(max_length=10, choices=FIELD_TYPE)
    form = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __str__(self):
        return self.type


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


