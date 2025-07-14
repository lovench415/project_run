from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Run(models.Model):
    STATUS_RUN = [('init', 'Забег инициализирован'), ('in_progress', 'Забег начат'), ('finished', 'Забег закончен')]
    athlete = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    status = models.CharField(choices=STATUS_RUN, default='init')


class AthleteInfo(models.Model):
    goals = models.TextField(default='')
    weight = models.PositiveSmallIntegerField(default=0)
    athlete = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)