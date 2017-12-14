from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = model.CharField(max_length=200)
    pub_date = model.DateTimeField("date published")
