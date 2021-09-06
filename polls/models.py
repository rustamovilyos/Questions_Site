from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    nomi = models.CharField(max_length=45)

    def __str__(self):
        return self.nomi


class Questions(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quiz_text = models.CharField(max_length=500)

    def __str__(self):
        return self.quiz_text


class Choice(models.Model):
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=150)
    correct = models.BooleanField()

    def __str__(self):
        return self.answer_text


class Result(models.Model):
    subject = models.ForeignKey(Category, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.FloatField(default=0.0)
