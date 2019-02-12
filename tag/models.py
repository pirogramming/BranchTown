from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    # TODO BooleanField 추가 해서 관심사와 tag 구분

    def __str__(self):
        return self.name
