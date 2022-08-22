from django.db import models


class NewTask(models.Model):
    title = models.CharField(max_length=200)
