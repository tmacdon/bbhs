from django.db import models
from django.utils import timezone

class Patient(models.Model):
    patient_id = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    

class PHQ9(models.Model):
    ANSWER_CHOICES=(
        ('0','Not at all'),
        ('1','Several Days'),
        ('2','More than half the days'),
        ('3','Nearly every day')
    )


    q1q='Little interest or plesure in doing things'
    q1a=models.IntegerField(
        choices=ANSWER_CHOICES,
        default=0,
    )

    def score(self):
        return 0
    def __str__(self):
        return "PHQ9 score:" + self.score
