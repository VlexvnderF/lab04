from msilib.schema import Class
from django.db import models

# Create your models here.
class Region2(models.Model):
    region_nom = models.CharField(max_length=200) 
    pub_date = models.DateTimeField('date published')
    
class Candidato2(models.Model):
    region = models.ForeignKey(Region2, on_delete=models.CASCADE)
    nom_cand=models.CharField(max_length=100)
    ape_cand=models.CharField(max_length=100)
    edad_cand=models.IntegerField(4)
    



