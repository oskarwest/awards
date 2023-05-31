import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
   #el atributo id, lo crea django automaticamente
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
    def was_published_recently__(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE) #el on_delete actua eliminando en cascada las respuestas de la pregunta.
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text