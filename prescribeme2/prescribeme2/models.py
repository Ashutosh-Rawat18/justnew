from django.db import models

# Create your models here.


class DocModel(models.Model):
    docname = models.CharField(max_length=150)
    age = models.IntegerField()
    email = models.CharField(max_length=150)
    phoneno = models.IntegerField()
    address = models.CharField(max_length=500)
    licenseno = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

    class Meta:
        db_table = "doctor"


class Premodel(models.Model):
    docname = models.CharField(max_length=150)
    symptom = models.CharField(max_length=150)
    dates = models.CharField(max_length=20)
    medicine1 = models.CharField(max_length=50)
    when1 = models.CharField(max_length=50)
    medicine2 = models.CharField(max_length=50)
    when2 = models.CharField(max_length=50)

    class Meta:
        db_table = "prescription"
