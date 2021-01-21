from django.db import models

# Create your models here.
# 1 step

class Question(models.Model):
    """
    Every question calss should have question text and pub date
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self): # whenever we call/use the object, it will return the question text
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #connected to question

    def __str__(self):# whenever we call/use the object, it will return the choice_text
        return self.choice_text