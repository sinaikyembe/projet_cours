from django.db import models

# Create your models here.
class Promotion(models.Model):
    name =models.CharField(max_length=30)

class Enseignant(models.Model):
    name = models.CharField(max_length=30)
    Grade =models.CharField(max_length=30)

class Cours(models.Model):
    # CREATE TABLE
    name =models.CharField(max_length=30)
    credit =models.IntegerField()
    volume_horaire = models.IntegerField()
    enseignant =models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    promotion =models.ForeignKey(Promotion, on_delete=models.CASCADE)


