from django.db import models

class Question(models.Model):
   #el atributo id, lo crea django automaticamente
    question_text=models.CharField(max_length=200)
    pud_date=models.DateTimeField("date published")

class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE) #el on_delete actua eliminando en cascada las respuestas de la pregunta.
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
