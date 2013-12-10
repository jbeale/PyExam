from django.db import models

class Item(models.Model):
    question_type = models.CharField(max_length=200)
    question_text = models.TextField()
    answer1 = models.CharField(max_length=254)
    answer2 = models.CharField(max_length=254)
    answer3 = models.CharField(max_length=254)
    answer4 = models.CharField(max_length=254)
    correctAns = models.CharField(max_length=254)
    explanation = models.TextField()

class Activity(models.Model):
    activity_name = models.CharField(max_length=254)
    activity_description = models.TextField()
    itemsList = models.TextField()

class Take(models.Model):
    studentId = models.CharField(max_length=254)
    activity = models.ForeignKey(Activity)
    date = models.DateTimeField()
    currentQuestion = models.IntegerField()
    currentScore = models.IntegerField()
    possibleScore = models.IntegerField()
    complete = models.BooleanField()