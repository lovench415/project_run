from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Run(models.Model):
    athlete = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
