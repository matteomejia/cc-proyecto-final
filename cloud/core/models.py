from django.db import models

# Create your models here.
class CeleryResult(models.Model):
    results = models.JSONField(blank=True, null=True)