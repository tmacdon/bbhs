from django.db import models
from django.utils import timezone

class Patient(models.Model):
    id= models.AutoField(primary_key=True)
    demographic_no = models.IntegerField(max_length=10) # This is the key from oscar
    title = models.CharField(max_length=10,blank=True)
    last_name = models.CharField(max_length=30,)
    first_name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=20)
    postal = models.CharField(max_length=9)
    phone = models.CharField(max_length=20,blank=True)
    phone2 = models.CharField(max_length=20,blank=True)
    email = models.EmailField(max_length=100)
    year_of_birth = models.CharField(max_length=4)
    month_of_birth = models.CharField(max_length=2)
    day_of_birth = models.CharField(max_length=2)
    hin = models.CharField(max_length=20) #helath card number
    ver = models.CharField(max_length=3, blank=True)
    chart_no = models.CharField(max_length=10, blank=True)
    spoken_lang = models.CharField(max_length=60, blank=True)
    provider_no = models.CharField(max_length=250, blank=True)
    sex = models.CharField(max_length=1)
    family_doctor = models.CharField(max_length=80, blank=True)
    sin = models.CharField(max_length=15, blank=True)

class PHQ9(models.Model):
    ANSWER_CHOICES=(
        ('0','Not at all'),
        ('1','Several Days'),
        ('2','More than half the days'),
        ('3','Nearly every day')
    )


    q1q='Little interest or plesure in doing things'
    q1a=models.TextField(
        choices=ANSWER_CHOICES,
        default=0,
    )

    def score(self):
        return 0
    def __str__(self):
        return "PHQ9 score:"
