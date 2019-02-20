from django.db import models
from django.conf import settings
from survey.models import Survey

<<<<<<< HEAD
=======

>>>>>>> f17008f429dec73ba4e8a8288f23dd69daa778c5
class Response(models.Model):
    respondent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
<<<<<<< HEAD
        return self.respondent
=======
        return str(self.respondent)
>>>>>>> f17008f429dec73ba4e8a8288f23dd69daa778c5
