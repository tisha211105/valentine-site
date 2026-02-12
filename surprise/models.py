from django.db import models

class Reason(models.Model):
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text
