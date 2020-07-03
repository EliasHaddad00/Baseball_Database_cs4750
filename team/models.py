from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


# Create your models here.
class editTeam(models.Model):
    team_name=models.CharField(max_length=50, default='')
    wins = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])
    losses = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])
    players = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])

    def __str__(self):
        return self.team_name

    def get_absolute_url(self):
        return reverse('team:editTeam')
