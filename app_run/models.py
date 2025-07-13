from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Run(models.Model):
    STATUS_RUN = [('INIT', 'Забег инициализирован'), ('IN_PROGRESS', 'Забег начат'), ('FINISHED', 'Забег закончен')]
    athlete = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    status = models.CharField(choices=STATUS_RUN, default='INIT')
